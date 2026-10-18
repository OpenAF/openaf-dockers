#!/usr/bin/env python3
"""Opt-in local-image tests: python3 integration.py --image IMAGE [--shell bash|zsh].
No implicit pulls. --network adds a missing-package request using remote repositories.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import tempfile
import time
import uuid
import zipfile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--image', required=True)
parser.add_argument('--shell', choices=['bash', 'zsh'], default='bash')
parser.add_argument('--network', action='store_true')
args = parser.parse_args()
docker = shutil.which('docker')
identity = subprocess.check_output([docker, 'image', 'inspect', args.image,
                                   '--format', '{{json .RepoDigests}} {{.Id}} {{.Os}}/{{.Architecture}}'], text=True).strip()
print('Image:', identity, flush=True)
wrapper = ROOT / 'bin' / ('openaf-docker.' + args.shell)
with tempfile.TemporaryDirectory(prefix='openaf-cli-integration-') as temporary:
    work = Path(temporary)
    (work / 'inputs').mkdir()
    (work / 'outputs').mkdir()
    (work / 'inputs/data.json').write_text('{"value":42}')
    (work / 'inputs/data.csv').write_text('name,value\none,42\n')
    shutil.copy(ROOT / 'tests/fixtures/process.js', work / 'process.js')
    shutil.copy(ROOT / 'tests/fixtures/process.yaml', work / 'process.yaml')
    env = {k: v for k, v in os.environ.items() if not k.startswith(('OPENAF_DOCKER_', 'OPACKS', 'OAF_JARGS'))}
    env.update(OPENAF_DOCKER_IMAGE=args.image, OPENAF_DOCKER_TTY='never')
    def run(*command, extra=None, data=b'', success=True):
        result = subprocess.run([str(wrapper), *command], cwd=work, env=dict(env, **(extra or {})),
                                input=data, capture_output=True, timeout=120)
        if success and result.returncode:
            raise AssertionError((command, result.returncode, result.stdout, result.stderr))
        return result
    def passed(name):
        print('PASS:', name, flush=True)
    result = run('oafp', 'file=inputs/data.json', 'out=json')
    assert json.loads(result.stdout) == {'value': 42}, result
    result = run('oafp', 'file=inputs/data.csv', 'in=csv', 'out=json')
    assert json.loads(result.stdout)[0]['name'] == 'one', result
    run('oafp', 'file=inputs/data.json', 'out=json', 'outfile=outputs/data.json')
    assert json.loads((work / 'outputs/data.json').read_text()) == {'value': 42}
    with (work / 'outputs/redirect.json').open('wb') as output:
        result = subprocess.run([str(wrapper), 'oafp', 'file=inputs/data.json', 'out=json'],
                                cwd=work, env=env, stdout=output, stderr=subprocess.PIPE, timeout=120)
    assert result.returncode == 0, result.stderr
    assert json.loads((work / 'outputs/redirect.json').read_text()) == {'value': 42}
    passed('JSON, CSV, nested outfile, host redirection')
    for selector, filename, output in [('openaf', 'process.js', 'script.json'), ('ojob', 'process.yaml', 'job.json')]:
        command = [selector, '-f', filename] if selector == 'openaf' else [selector, filename]
        run(*command)
        assert json.loads((work / 'outputs' / output).read_text()) == {'value': 42, 'processed': True}
    passed('openaf -f and ojob relative file operations')
    result = run('openaf', '-c', 'print(java.lang.System.getProperty("cli.probe"))', extra={'OAF_JARGS': '-Dcli.probe=ok'})
    assert result.stdout.strip() == b'ok', result
    result = run('openaf', '-c', 'print(getEnv("HOME")); print(java.lang.System.getProperty("user.home")); io.writeFileString(getEnv("HOME")+"/probe", "ok");',
                 extra={'OPENAF_DOCKER_USER': '12345:23456'})
    home, java_home = result.stdout.decode().splitlines()
    assert home == java_home and home.startswith('/tmp/openaf-cli.'), result
    passed('OAF_JARGS, non-image UID and writable Java home')
    result = run('openaf', '-c', 'print(getEnv("OPACKS") === ""); print(getEnv("OPACKS_DB") === "")',
                 extra={'OPACKS': '', 'OPACKS_DB': '', 'OPACKS_DIR': ''})
    assert result.stdout.splitlines() == [b'true', b'true'], result
    result = run('openaf', '-c', 'print("application-started")', extra={'OPACKS_DIR': str(ROOT / 'tests/fixtures/opacks')})
    # A second invocation installs and loads its own private package.
    result = run('openaf', '-c', 'loadLib("probe.js"); print(cliProbe())',
                 extra={'OPACKS_DIR': str(ROOT / 'tests/fixtures/opacks')})
    assert result.stdout.strip() == b'local-opack-ok', result
    assert result.stderr, 'bootstrap diagnostics should be on stderr'
    archives = work / 'archive packages'
    archives.mkdir()
    with zipfile.ZipFile(archives / 'CLIProbe.opack', 'w') as archive:
        for source in (ROOT / 'tests/fixtures/opacks/CLIProbe').iterdir():
            archive.write(source, source.name)
    result = run('oafp', 'file=inputs/data.json', 'out=json', extra={'OPACKS_DIR': str(archives)})
    assert json.loads(result.stdout) == {'value': 42}, result
    assert result.stderr, result
    passed('local directory/archive oPacks, clean stdout, empty variables')
    broken = work / 'broken'
    (broken / 'BadCLI').mkdir(parents=True)
    (broken / 'BadCLI/.package.yaml').write_text('name: BadCLI\nversion: "1"\nfiles: [missing.js]\nscripts:\n  preinstall: "throw new Error(\'deliberate bootstrap failure\')"\ndependencies: {}\n')
    result = run('openaf', '-c', 'print("must-not-run")', extra={'OPACKS_DIR': str(broken)}, success=False)
    assert result.returncode != 0 and b'must-not-run' not in result.stdout, result
    passed('failed local bootstrap prevents application')
    # Database-only configuration must be visible within this invocation, without network IO.
    database = work / 'local-repository'
    database.mkdir()
    with zipfile.ZipFile(database / 'opack.db', 'w') as archive:
        archive.writestr('packages.json', json.dumps({'CLIRepositoryProbe': {'name': 'CLIRepositoryProbe', 'version': '1'}}))
    result = run('openaf', '-c', 'noHomeComms=true; print(getOPackRemoteDB().CLIRepositoryProbe.name); print(getEnv("OPACKS_DB"))',
                 extra={'OPACKS_DB': '/work/local-repository'})
    assert result.stdout.splitlines() == [b'CLIRepositoryProbe', b'/work/local-repository'], result
    passed('database-only bootstrap')
    result = subprocess.run([docker, 'run', '--rm', '--entrypoint', '/bin/sh',
                             '--mount', 'type=bind,src=' + str(ROOT / 'installOPacks.js') + ',dst=/corrected-helper.js,readonly',
                             '--mount', 'type=bind,src=' + str(ROOT / 'tests/fixtures/opacks') + ',dst=/pkgs,readonly',
                             '--env', 'OPACKS_DIR=/pkgs', args.image, '-c',
                             '/openaf/openaf -f /corrected-helper.js >&2 && /openaf/openaf -c \'print(getOPackPath("CLIProbe"))\''],
                            capture_output=True, timeout=120)
    assert result.returncode == 0 and b'/openaf/CLIProbe' in result.stdout, result
    passed('repository helper directory-field regression without compatibility adapter')

    result = run('oafp', 'in=json', 'out=json', data=b'{"piped":true}\n')
    assert json.loads(result.stdout) == {'piped': True}, result
    result = run('openaf', '-c', 'exit(37)', success=False)
    assert result.returncode == 37, result
    result = run('openaf', '-c', 'io.writeFileString("outputs/forbidden", "bad")',
                 extra={'OPENAF_DOCKER_READONLY': 'true'}, success=False)
    assert not (work / 'outputs/forbidden').exists(), result
    result = run('oafp', 'file=inputs/data.json', 'out=json', extra={'OPENAF_DOCKER_READONLY': 'true'})
    assert json.loads(result.stdout) == {'value': 42}
    passed('pipeline, status propagation, read-only workspace')
    if os.uname().sysname == 'Linux' and 'microsoft' not in os.uname().release.lower():
        assert (work / 'outputs/script.json').stat().st_uid == os.getuid()
        passed('host output ownership (requires ordinary, non-remapped Docker)')
    else:
        print('SKIP: ordinary Linux output ownership; current host is not ordinary Linux', flush=True)
    # Test-only docker proxy adds a unique label to discover and clean containers.
    mockbin = work / 'proxy'
    mockbin.mkdir()
    label = 'openaf-cli-test=' + uuid.uuid4().hex
    proxy = mockbin / 'docker'
    proxy.write_text('#!/usr/bin/env python3\nimport os,sys\nos.execv(' + repr(docker) + ', [' + repr(docker) + ', sys.argv[1], "--label", ' + repr(label) + '] + sys.argv[2:])\n')
    proxy.chmod(0o755)
    signal_env = dict(env, PATH=str(mockbin) + os.pathsep + env['PATH'])
    def containers():
        return subprocess.check_output([docker, 'ps', '-aq', '--filter', 'label=' + label], text=True).split()
    try:
        for phase in ('application', 'bootstrap'):
            if phase == 'bootstrap':
                slow = work / 'slow' / 'SlowCLI'
                slow.mkdir(parents=True)
                (slow / '.package.yaml').write_text('name: SlowCLI\nversion: "1"\nfiles: []\ndependencies: {}\nscripts:\n  preinstall: \'printErr("SIGNAL_READY"); sleep(60000);\'\n')
            for sig in (signal.SIGINT, signal.SIGTERM):
                test_env = dict(signal_env)
                if phase == 'bootstrap':
                    test_env['OPACKS_DIR'] = str(slow.parent)
                proc = subprocess.Popen([str(wrapper), 'openaf', '-c', 'printErr("SIGNAL_READY"); sleep(60000)'],
                                        cwd=work, env=test_env, stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                try:
                    # Wait for an actual readiness line, with a deadline.
                    import selectors
                    sel = selectors.DefaultSelector()
                    sel.register(proc.stderr, selectors.EVENT_READ)
                    deadline = time.monotonic() + 60
                    ready = False
                    readiness = b''
                    while time.monotonic() < deadline and proc.poll() is None:
                        if sel.select(0.2):
                            readiness += os.read(proc.stderr.fileno(), 65536)
                            if b'SIGNAL_READY' in readiness:
                                ready = True
                                break
                    sel.close()
                    assert ready, 'signal fixture did not become ready'
                    proc.send_signal(sig)
                    stdout, stderr = proc.communicate(timeout=15)
                    assert proc.returncode != 0, (phase, sig, stdout, stderr)
                    deadline = time.monotonic() + 10
                    while containers() and time.monotonic() < deadline:
                        time.sleep(0.1)
                    assert not containers(), 'interrupted container was not removed'
                    passed('%s %s and container cleanup' % (phase, sig.name))
                finally:
                    if proc.poll() is None:
                        proc.kill()
                        proc.communicate()
    finally:
        for container in containers():
            subprocess.run([docker, 'rm', '-f', container], check=True, stdout=subprocess.DEVNULL)
    if args.network:
        result = run('openaf', '-c', 'print("must-not-run")', extra={'OPACKS': 'DOES_NOT_EXIST_OPENAF_CLI_728139'}, success=False)
        assert result.returncode != 0 and b'must-not-run' not in result.stdout, result
        passed('missing remote package stops execution')
    else:
        print('SKIP: remote-package and OAF_ORIG network behavior (not requested)', flush=True)
print('Integration checks passed:', args.shell, flush=True)
