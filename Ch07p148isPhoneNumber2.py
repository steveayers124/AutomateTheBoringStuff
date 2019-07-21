# Using regex, determine whether a passed string is a phone number.
import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

line1 = '415-555-4242 is a phone number:'
matchObj = phoneNumRegex.search(line1)
print('Searching:|'+line1+'|\n'+'Phone number found:|'+matchObj.group()+'|')

line1 = 'Moshi moshi is a phone number:'
matchObj = phoneNumRegex.search(line1)
if matchObj is not None:
    print('Searching:|'+line1+'|\n'+'Phone number found:|'+matchObj.group()+'|')

line1 = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my offfice.'
matchObj = phoneNumRegex.search(line1)
print('Searching:|'+line1+'|\n'+'Phone number found:|'+matchObj.group()+'|')
print('Done. ' + 'Now define group parts, and access parts, or whole.')

r = re.compile(r'(\d{3})-(\d{3}-\d{4})')
line1 = 'My number is 415-555-4242.'
m = r.search(line1)
if m is not None:
    print('Searching |' + line1 + '| for pattern |' + str(r.pattern) + '|')
    print(m.group(1))
    print(m.group(2))
    print(m.group(0))
    print(m.group())
print('Done. ' + 'Now multiple-assign that tuple.')
if m is not None:
    print(m.groups())
    areaCode, mainNumber = m.groups()
    print('The areacode was ' + areaCode + ', and the main number was ' + mainNumber + '.')
print('Done. ' + 'Now how do you deal with real parens?')

p = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
line1 = 'My number is (415) 555-4242.'
m = p.search(line1)
if m is not None:
    print(m.group(1))
    print(m.group(2))
print('Done. ' + 'Now for ignoring case sensitivity...')

robocop = [re.compile('RoboCop'),
           re.compile('ROBOCOP'),
           re.compile('RobOCop'),
           re.compile('RobocOp'), ]
line = ['RoboCop is part man, part machine, all cop.',
        'ROBOCOP protects the innocent.',
        'Al, why does your programming book talk about robocop so much?']
for c in range(len(robocop)):
    for l in range(len(line)):
        found = robocop[c].search(line[l])
        if found is not None:
            print(found.group() + ', pattern |' + robocop[c].pattern + '|, line |' + line[l] + '|')
print('Done. ' + 'Okay, that ^ was all case sensitive. Default behavior.')
print('What follows is case insensitive, using the re.IGNORECASE flag, or re.I for short.')

robocop = [re.compile('RoboCop', re.IGNORECASE),
           re.compile('ROBOCOP', re.I),
           re.compile('RobOCop', re.I),
           re.compile('RobocOp', re.I), ]
line = ['RoboCop is part man, part machine, all cop.',
        'ROBOCOP protects the innocent.',
        'Al, why does your programming book talk about robocop so much?']
for c in range(len(robocop)):
    for l in range(len(line)):
        found = robocop[c].search(line[l])
        if found is not None:
            print(found.group() + ', pattern |' + robocop[c].pattern + '|, line |' + line[l] + '|')
print('Done. Now, let\'s substitute strings for the found pattern.')
