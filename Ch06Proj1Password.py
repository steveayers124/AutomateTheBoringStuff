#! python3
# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'laskdy091832i4erfakljsldiuvs4uyot2358irp0-guw9vjhr8bn ',
             'blog': 'z.x,mcnvaksdjhfpvo9384hglku34yfhlakenr',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python3 Ch06Proj1Password.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]    # first command line arg is the account name
print(sys.version)
print(sys.version_info)
print(sys.api_version)

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
