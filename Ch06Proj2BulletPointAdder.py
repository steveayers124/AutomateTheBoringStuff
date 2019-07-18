#! python3
# Ch06Proj2BulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# text = 'Separate lines and add stars.'
lines = text.split('\n')
text = ''
for n in lines:
    text += '* ' + n + '\n'
pyperclip.copy(text)
