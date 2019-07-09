# Use the dictionary datatype's .setdefault() method to aid in counting incidence of
# symbols in a string.

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}
for symbol in message:
    count.setdefault(symbol, 0)
    count[symbol] += 1

# pprint.pprint(count)

formatted = pprint.pformat(count)

print(formatted)
