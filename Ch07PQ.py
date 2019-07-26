import re

Nakamoto = re.compile(r'[A-Z][a-z]*\sNakamoto')

a = 'Satoshi Nakamoto'
b = 'Alice Nakamoto'
c = 'RoboCop Nakamoto'
d = 'Mr. Nakamoto'
e = 'Nakamoto'
f = 'Satoshi nakamoto'
testStrings = [a,b,c,d,e,f]

for s in range(len(testStrings)):
    matchObj = Nakamoto.search(testStrings[s])
    if matchObj is not None:
        print('Searching:|'+testStrings[s]+'|\n'+'Name found:|'+matchObj.group()+'|')
    else:
        print('Searching:|'+testStrings[s]+'|\n'+'No match with first name was found.')

