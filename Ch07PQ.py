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

whoDoesWhat = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)
sentences = [
    'Alice eats apples.',
    'Bob pets cats.',
    'Carol throws baseballs.',
    'Alice throws Apples.',
    'BOB EATS CATS.',
    'RoboCop eats apples.',
    'ALICE THROWS FOOTBALLS.',
    'Carol eats 7 cats.'
]
print('Testing the following lines against the who-does-what sentence testing regex with pattern:')
print(whoDoesWhat.pattern)
for line in range(len(sentences)):
    matchObj = whoDoesWhat.search(sentences[line])
    if matchObj is not None:
        printMatch = "That's a perfect match!"
    else:
        printMatch = "Sorry. That sentence doesn't match the pattern."
    print('|' + str(sentences[line]) + '| --> result: ' + printMatch)
