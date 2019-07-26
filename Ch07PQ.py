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

###################################
# example of implementing switch case functionality in Python 3
# Use of default allows you to give the 'else' portion of the statement.
# When the expected value isn't present, None results.
case = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
print(case.get('b', -1))
print(case.get('b'))
print(case.get('b', 0))
print(case.get('z', -1))
print(case.get('z'))
print(case.get('z', 0))
# Output:
# 2
# 2
# 2
# -1
# None
# 0
###################################


