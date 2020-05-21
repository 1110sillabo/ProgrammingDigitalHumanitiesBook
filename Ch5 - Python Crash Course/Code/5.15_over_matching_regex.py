import re

# author1 = ’[A-Z][a-z]*’
# author2 = ‘[a-zA-Z]*’
# author3 = ‘\S*’
# author4 = ‘\w*’.

authorregex = 'INSERT ONE OF THE AUTHOR REGEXES ABOVE'
sampletext = ('The biggest contribution is Master (2001).'
    'Its impact cannot be denied, on pain of miSbeHaving.')
match = re.findall(authorregex,sampletext)
print(match)
