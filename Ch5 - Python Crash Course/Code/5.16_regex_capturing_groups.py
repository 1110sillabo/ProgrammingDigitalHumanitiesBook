import re
capturingauthordate = '([A-Z][a-z]*)\s\((\d\d\d\d)\)'
sampletext = ('The biggest contribution is Master (2001).'
    'Its impact cannot be denied, on pain of miSbeHaving.')
capturingmatch = re.findall(capturingauthordate,sampletext)
for item in capturingmatch:
    print(item[0] + ' ' + item[1])
