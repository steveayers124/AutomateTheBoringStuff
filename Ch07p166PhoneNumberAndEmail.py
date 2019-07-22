# Ch07p166PhoneNumberAndEmail.py: find all phone numbers and email addresses in text copied to the system clipboard,
# and replace what's on the clipboard with just the possible phone and email items.

import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?             # area code
    (\s|-|\.)?                     # separator
    \d{3}                          # first 3 digits
    (\s|-|\.)                      # separator
    \d{4}                          # last 4 digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE | re.I)
# TODO: compile an email regex


# TODO: get text to search from clipboard

# TODO: search text, capturing phones
# TODO: search text, capturing emails

# TODO: put just the phones and emails text to clipboard

