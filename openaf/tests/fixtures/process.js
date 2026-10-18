var value = io.readFileJSON('inputs/data.json');
value.processed = true;
io.writeFileJSON('outputs/script.json', value);
print(stringify(value, undefined, ''));
