# Ch07p166PhoneNumberAndEmail.py: find all phone numbers and email addresses in text copied to the system clipboard,
# and replace what's on the clipboard with just the possible phone and email items.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # area code
    (\s|-|\.)?                       # separator
    (\d{3})                          # first 3 digits
    (\s|-|\.)                        # separator
    (\d{4})                          # last 4 digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE | re.I)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9.\-_+%]+               # email name
    @                                # at symbol
    [a-zA-Z0-9.\-]+                  # domain name
    (\.[a-zA-Z]{2,4})                # dot something
    )''', re.VERBOSE)
# line1 = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# print(phoneRegex.findall(line1))
# line2 = 'Email me at adam@cox.net tomorrow. adam@home.com is my office.'
# # found = emailRegex.search(line2)
# # if found is not None:
# #     found = found.group()
# # else:
# #     found = []
# # print(str(found) + ', pattern |' + emailRegex.pattern + '|, line |' + line2 + '|')
# print(emailRegex.findall(line2))

# Find matches in clipboard text.
'''
800-420-7240
415-863-9100
415-863-9150
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
'''

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

print(matches)

# TODO: put just the phones and emails text to clipboard

