#!/usr/bin/env python3
"""Offline contract tests; no Docker daemon, OpenAF or third-party Python packages."""
import json
import os
from pathlib import Path
import pty
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CLI(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="openaf-cli-")
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.work = self.base / "work space:'$"
        self.work.mkdir()
        self.bin = self.base / 'mock'
        self.bin.mkdir()
        self.capture = self.base / 'capture.json'
        mock = self.bin / 'docker'
        mock.write_text('''#!/usr/bin/env python3
import json, os, sys
from pathlib import Path
Path(os.environ['CAPTURE']).write_text(json.dumps({'argv': sys.argv[1:], 'env': dict(os.environ)}))
if os.environ.get('MOCK_STREAM'):
    sys.stdout.buffer.write(sys.stdin.buffer.read())
    sys.stderr.write('application stderr\\n')
sys.exit(int(os.environ.get('MOCK_STATUS', '0')))
''')
        mock.chmod(0o755)
        self.env = {k: v for k, v in os.environ.items() if k in ('PATH', 'LANG', 'TMPDIR', 'SYSTEMROOT')}
        self.env.update(PATH=str(self.bin) + os.pathsep + os.environ['PATH'],
                        HOME=str(self.base), CAPTURE=str(self.capture))
        self.shells = [s for s in ('bash', 'zsh') if shutil.which(s)]

    def run_cli(self, shell, *args, env=None, cwd=None, script=None, data=b''):
        return subprocess.run([str(script or ROOT / 'bin' / ('openaf-docker.' + shell)), *args],
                              env=dict(self.env, **(env or {})), cwd=cwd or self.work,
                              input=data, capture_output=True)

    def captured(self):
        return json.loads(self.capture.read_text())

    def test_dispatch_and_exact_argv(self):
        values = ['', 'a b', '"quotes"', "'single'", 'line\nbreak', '$HOME', '*', '$(touch UNEXPECTED)', '`touch UNEXPECTED`', '--help']
        for shell in self.shells:
            for selector in ('openaf', 'oaf', 'oafp', 'ojob'):
                with self.subTest(shell=shell, selector=selector):
                    expected_selector = 'openaf' if selector == 'oaf' else selector
                    result = self.run_cli(shell, selector, *values)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    argv = self.captured()['argv']
                    marker = argv.index('openaf-cli')
                    self.assertEqual(argv[marker + 1:], [expected_selector, *values])
                    self.assertEqual(argv[argv.index('--entrypoint') + 1], '/bin/sh')
                    self.assertEqual(argv[marker - 2], '-c')
                    self.assertFalse((self.work / 'UNEXPECTED').exists())
                    link = self.base / selector
                    link.unlink(missing_ok=True)
                    link.symlink_to(ROOT / 'bin' / ('openaf-docker.' + shell))
                    self.assertEqual(self.run_cli(shell, '-h', script=link).returncode, 0)
                    self.assertEqual(self.captured()['argv'][-2:], [expected_selector, '-h'])
            self.assertEqual(self.run_cli(shell, '--help').returncode, 0)
            self.assertEqual(self.run_cli(shell, 'invalid').returncode, 2)
            self.assertEqual(self.run_cli(shell).returncode, 2)

    def test_mounts_config_and_environment(self):
        for shell in self.shells:
            opacks = self.base / 'outside packages'
            opacks.mkdir(exist_ok=True)
            env = dict(OAF_JARGS='-Dtest=a\nb', OPACKS='', OPACKS_DB='', OPACKS_DIR=str(opacks),
                       EXTRA='line1\nline2', EMPTY='', SECRET='not forwarded', TERM='xterm',
                       OPENAF_DOCKER_ENV='EXTRA,EMPTY,UNSET,EXTRA',
                       OPENAF_DOCKER_IMAGE='example/image@sha256:' + 'a' * 64,
                       OPENAF_DOCKER_READONLY='true', OPENAF_DOCKER_USER='12345:6789')
            result = self.run_cli(shell, 'oafp', env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            argv = self.captured()['argv']
            self.assertIn('type=bind,src=' + str(self.work.resolve()) + ',dst=/work,readonly', argv)
            self.assertIn('type=bind,src=' + str(opacks.resolve()) + ',dst=/_openaf_cli/opacks,readonly', argv)
            self.assertIn('OPACKS_DIR=/_openaf_cli/opacks', argv)
            names = [argv[i + 1] for i, a in enumerate(argv[:-1]) if a == '--env']
            self.assertEqual(names.count('EXTRA'), 1)
            for name in ('OAF_JARGS', 'OPACKS', 'OPACKS_DB', 'EMPTY', 'TERM'):
                self.assertIn(name, names)
            for name in ('SECRET', 'HOME', 'PATH', 'UNSET'):
                self.assertNotIn(name, names)
            self.assertIn('12345:6789', argv)
            self.assertEqual(self.captured()['env']['EXTRA'], env['EXTRA'])
            self.assertNotIn('--tty', argv)
            self.assertEqual(self.run_cli(shell, 'ojob', env={'OPENAF_DOCKER_USER': 'image'}).returncode, 0)
            self.assertNotIn('--user', self.captured()['argv'])
            other = self.base / ('other-' + shell)
            other.mkdir()
            link = self.base / ('cwd-link-' + shell)
            link.symlink_to(other)
            self.assertEqual(self.run_cli(shell, 'openaf', cwd=link).returncode, 0)
            self.assertIn('type=bind,src=' + str(other.resolve()) + ',dst=/work', self.captured()['argv'])
            self.assertEqual(self.run_cli(shell, 'openaf', env={'OPACKS_DIR': '.'}).returncode, 0)
            self.assertIn('type=bind,src=' + str(self.work.resolve()) + ',dst=/_openaf_cli/opacks,readonly', self.captured()['argv'])

    def test_invalid_configuration(self):
        invalid = [('OPENAF_DOCKER_IMAGE', ''), ('OPENAF_DOCKER_IMAGE', '-bad'),
                   ('OPENAF_DOCKER_READONLY', 'yes'), ('OPENAF_DOCKER_TTY', ''),
                   ('OPENAF_DOCKER_USER', '0'), ('OPENAF_DOCKER_USER', ':1'),
                   ('OPENAF_DOCKER_USER', '1:2:3'), ('OPACKS_DIR', '/nonexistent-openaf-cli'),
                   ('OPENAF_DOCKER_ENV', 'A,,B'), ('OPENAF_DOCKER_ENV', 'A,'),
                   ('OPENAF_DOCKER_ENV', 'x=y'), ('OPENAF_DOCKER_ENV', '1NAME')]
        invalid += [('OPENAF_DOCKER_ENV', name) for name in
                    ('HOME', 'PATH', 'OPENAF', 'OAFP', 'OJOB', 'OPACK_EXEC', 'OPACKS_DIR',
                     'OAF_HOME', 'OAF_DIR', 'OAF_OPACKS', 'JAVA_HOME', 'OPENAF_DOCKER_FAKE', 'OPENAF_CLI_X', 'TINI_X', 'BASH_ENV')]
        for shell in self.shells:
            for key, value in invalid:
                with self.subTest(shell=shell, key=key, value=value):
                    self.assertEqual(self.run_cli(shell, 'openaf', env={key: value}).returncode, 2)
            self.assertEqual(self.run_cli(shell, 'openaf', cwd='/').returncode, 2)
            self.assertEqual(self.run_cli(shell, 'openaf', env={'OPENAF_DOCKER_TTY': 'always'}).returncode, 2)
            for char in (',', '"', '\n', '\r', 'end\n'):
                directory = self.base / ('bad' + shell + char)
                directory.mkdir()
                self.assertEqual(self.run_cli(shell, 'openaf', cwd=directory).returncode, 2)

    def test_streams_status_and_missing_docker(self):
        data = bytes(range(256)) * 4096
        for shell in self.shells:
            result = self.run_cli(shell, 'oafp', env={'MOCK_STREAM': '1', 'MOCK_STATUS': '37'}, data=data)
            self.assertEqual(result.returncode, 37)
            self.assertEqual(result.stdout, data)
            self.assertEqual(result.stderr, b'application stderr\n')
            self.assertEqual(self.run_cli(shell, 'oafp', env={'MOCK_STATUS': '125'}).returncode, 125)
            no_docker = self.base / ('no-docker-' + shell)
            no_docker.mkdir()
            # Invoke interpreter explicitly because env shebang needs PATH.
            result = subprocess.run([shutil.which(shell), str(ROOT / 'bin' / ('openaf-docker.' + shell)), 'oafp'],
                                    env=dict(self.env, PATH=str(no_docker)), capture_output=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn(b'docker executable not found', result.stderr)

    def test_tty_matrix(self):
        for shell in self.shells:
            for mode in ('auto', 'never', 'always'):
                for redirected in (None, 1, 2):
                    master, slave = pty.openpty()
                    try:
                        streams = [slave, slave, slave]
                        if redirected is not None:
                            streams[redirected] = subprocess.PIPE
                        process = subprocess.Popen([str(ROOT / 'bin' / ('openaf-docker.' + shell)), 'oafp'],
                                                   stdin=streams[0], stdout=streams[1], stderr=streams[2],
                                                   cwd=self.work, env=dict(self.env, OPENAF_DOCKER_TTY=mode))
                        process.communicate(timeout=15)
                        self.assertEqual(process.returncode, 0)
                        expected = mode == 'always' or (mode == 'auto' and redirected is None)
                        self.assertEqual('--tty' in self.captured()['argv'], expected)
                    finally:
                        os.close(master)
                        os.close(slave)

    def test_install_update_and_aliases(self):
        for shell in self.shells:
            with self.subTest(shell=shell):
                bindir = self.base / ("install ' " + shell)
                rc = self.base / ('rc-' + shell)
                rc.write_text('# unrelated\nexport KEEP_ME=yes\n')
                args = ['--bin-dir', str(bindir), '--rc-file', str(rc)]
                result = self.run_cli(shell, '--install', '--aliases', '--replace-aliases', *args)
                self.assertEqual(result.returncode, 0, result.stderr)
                content = rc.read_bytes()
                installed = bindir / ('openaf-docker.' + shell)
                self.assertEqual(installed.read_bytes(), (ROOT / 'bin' / installed.name).read_bytes())
                self.assertTrue(os.access(installed, os.X_OK))
                self.assertTrue((bindir / 'openaf-docker').is_symlink())
                self.assertEqual(self.run_cli(shell, '--update', '--replace-aliases', *args).returncode, 0)
                self.assertEqual(content, rc.read_bytes())
                self.assertEqual(len(list(self.base.glob('rc-' + shell + '.openaf-docker.backup.*'))), 1)
                self.assertIn(b'alias oaf=', content)
                # Update an existing managed block from before oaf was included.
                rc.write_bytes(b''.join(line for line in content.splitlines(keepends=True) if not line.startswith(b'alias oaf=')))
                old_content = rc.read_bytes()
                native_oaf = self.bin / 'oaf'
                native_oaf.write_text('#!/bin/sh\nexit 0\n')
                native_oaf.chmod(0o755)
                self.assertEqual(self.run_cli(shell, '--update', *args).returncode, 2)
                self.assertEqual(rc.read_bytes(), old_content)
                native_oaf.unlink()
                self.assertEqual(self.run_cli(shell, '--update', '--replace-aliases', *args).returncode, 0)
                self.assertEqual(content, rc.read_bytes())
                self.assertEqual(len(list(self.base.glob('rc-' + shell + '.openaf-docker.backup.*'))), 2)
                # Functions/aliases expand in an interactive shell; no real startup files used.
                commands = self.base / ('commands-' + shell)
                commands.write_text('OAF_JARGS="inline" oafp file=x\n')
                result = subprocess.run([shutil.which(shell), *(['--norc', '-ic'] if shell == 'bash' else ['-fic']), 'source "$1"\nsource "$2"', '_', str(rc), str(commands)],
                                        env=self.env, cwd=self.work, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(self.captured()['argv'][-2:], ['oafp', 'file=x'])
                self.assertEqual(self.captured()['env']['OAF_JARGS'], 'inline')
                commands.write_text('OAF_JARGS="inline" oaf --help\n')
                result = subprocess.run([shutil.which(shell), *(['--norc', '-ic'] if shell == 'bash' else ['-fic']), 'source "$1"\nsource "$2"', '_', str(rc), str(commands)],
                                        env=self.env, cwd=self.work, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(self.captured()['argv'][-2:], ['openaf', '--help'])
                rc.write_text(content.decode() + '\nalias oafp=other\n')
                self.assertEqual(self.run_cli(shell, '--update', *args).returncode, 2)
                rc.write_text('# >>> openaf-docker managed aliases >>>\n')
                self.assertEqual(self.run_cli(shell, '--update', *args).returncode, 2)
                installed.write_text('unrelated')
                self.assertEqual(self.run_cli(shell, '--update', *args).returncode, 2)

    def test_install_opt_in_and_collisions(self):
        bindir = self.base / 'installed'
        rc = self.base / 'startup'
        rc.write_text('# untouched\n')
        args = ['--bin-dir', str(bindir), '--rc-file', str(rc)]
        for shell in self.shells:
            result = self.run_cli(shell, '--install', *args)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(rc.read_text(), '# untouched\n')
            self.assertEqual(os.readlink(bindir / 'openaf-docker'), 'openaf-docker.' + shell)
            for name in ('oafp', 'oaf'):
                native = self.bin / name
                native.write_text('#!/bin/sh\nexit 0\n')
                native.chmod(0o755)
                self.assertEqual(self.run_cli(shell, '--install', '--aliases', *args).returncode, 2)
                self.assertEqual(rc.read_text(), '# untouched\n')
                native.unlink()
            rc.write_text('# <<< openaf-docker managed aliases <<<\n')
            self.assertEqual(self.run_cli(shell, '--install', '--aliases', *args).returncode, 2)
            rc.write_text('# untouched\n')
        (bindir / 'openaf-docker').unlink()
        (bindir / 'openaf-docker').write_text('unrelated')
        self.assertEqual(self.run_cli(self.shells[0], '--install', *args).returncode, 2)
        self.assertEqual((bindir / 'openaf-docker').read_text(), 'unrelated')

    def test_bootstrap_subprocess_contract(self):
        # Exercise the actual fixed shell program with fake launchers, without a daemon.
        for shell in self.shells:
            self.assertEqual(self.run_cli(shell, 'openaf').returncode, 0)
            argv = self.captured()['argv']
            program = argv[argv.index('openaf-cli') - 1]
            runtime = self.base / ('runtime-' + shell)
            runtime.mkdir()
            (runtime / '.docker').mkdir()
            (runtime / '.docker' / 'installOPacks.js').write_text('// fixture')
            launcher = '''#!/usr/bin/env python3
import json, os, sys
from pathlib import Path
if '-c' in sys.argv:
    assert sys.stdin.buffer.read() == b''
    Path(os.environ['BOOT_CAPTURE']).write_text(json.dumps({k: os.environ.get(k) for k in ('OPACKS', 'OPACKS_DIR', 'OPACKS_DB')}))
    print('bootstrap progress')
    sys.exit(int(os.environ.get('BOOT_STATUS', '0')))
sys.stdout.buffer.write(sys.stdin.buffer.read())
print('application', file=sys.stderr)
'''
            for tool in ('openaf', 'ojob', 'oafp'):
                (runtime / tool).write_text(launcher)
                (runtime / tool).chmod(0o755)
            passwd = self.base / ('passwd-' + shell)
            passwd.write_text('test:x:%s:%s:test:%s:/bin/sh\n' % (os.getuid(), os.getgid(), self.base))
            program = program.replace('/openaf/', str(runtime) + '/').replace('PATH=/openaf:', 'PATH=' + str(runtime) + ':').replace('[ -w /openaf ]', '[ -w ' + str(runtime) + ' ]').replace('/etc/passwd', str(passwd))
            capture = self.base / ('boot-' + shell)
            env = dict(self.env, BOOT_CAPTURE=str(capture))
            def run(extra):
                return subprocess.run(['/bin/sh', '-c', program, 'openaf-cli', 'oafp'],
                                      input=b'input\x00bytes', capture_output=True, env=dict(env, **extra))
            result = run({})
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(capture.exists())
            result = run({'OPACKS': '', 'OPACKS_DB': '', 'OPACKS_DIR': ''})
            self.assertEqual(result.stdout, b'input\x00bytes')
            self.assertFalse(capture.exists())
            for request in ({'OPACKS': 'one'}, {'OPACKS_DB': 'db'}, {'OAF_ORIG': ''}, {'OPACKS_DIR': 'dir'}):
                result = run(dict(OPACKS='', OPACKS_DB='', OPACKS_DIR='', **{}) | request)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, b'input\x00bytes')
                self.assertIn(b'bootstrap progress', result.stderr)
            (runtime / '.installed').touch()
            result = run({'OPACKS': 'two', 'BOOT_STATUS': '42'})
            self.assertEqual(result.returncode, 42)
            self.assertEqual(result.stdout, b'')
            self.assertNotIn(b'application', result.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
