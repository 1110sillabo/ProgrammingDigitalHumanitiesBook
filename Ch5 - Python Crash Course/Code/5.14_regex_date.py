import re

dateregex = '\d\d\d\d'
sampletext = ('The biggest contribution to the field is due to '
    'Master (2001) and its impac cannot be denied')
match = re.findall(dateregex,sampletext)
print(match)
