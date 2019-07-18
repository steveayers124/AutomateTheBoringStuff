#! python3
# Ch06Proj2BulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for n in range(len(lines)):
    lines[n] = '* ' + lines[n]
text = '\n'.join(lines)

pyperclip.copy(text)
