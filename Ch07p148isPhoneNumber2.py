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
print('Done')
