hello = 'Hello world!'
print(hello[1])    # e
print(hello[0:5])  # Hello
print(hello[:5])   # Hello
print(hello[3:])   # lo world!

print('Hello'.upper())
print('Hello'.upper().isupper())
print('Hello'.upper().lower())

print('Remember, remember, the fifth of November.'.split())  # ['Remember,','remember,','the','fifth','of','November.']
print('-'.join('There can be only one.'.split()))  # There-can-be-only-one.
