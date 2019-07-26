import re

Nakamoto = re.compile(r'[A-Z][a-z]*\sNakamoto')

a = 'Satoshi Nakamoto'
b = 'Alice Nakamoto'
c = 'RoboCop Nakamoto'
d = 'Mr. Nakamoto'
e = 'Nakamoto'
f = 'Satoshi nakamoto'

matchObj = Nakamoto.search(a)
if matchObj is not None:
    print('Searching:|'+a+'|\n'+'Name found:|'+matchObj.group()+'|')




