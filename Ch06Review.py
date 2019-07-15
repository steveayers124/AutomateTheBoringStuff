print('''
sq=|\'|
dq|\"|
tb|\t|
nl|\n|
''')


print(r'''
sq=|\'|
dq|\"|
tb|\t|
nl|\n|
''')


spam = 'There is a container of milk in the fridge'
eggs = 'It is labeled "Milk Experiment"'
ham = 'Please do not drink it'
sausage = 'Sincerely'
print('.  '.join([spam, eggs, ham, sausage]), end='.\n')
a = 'cats'
b = 'bats'
c = 'rats'
d = ['My', 'name', 'is', 'Simon']
print(', '.join([a, b, c]))
print(' '.join(d))
print('ABC'.join(d))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.

Sincerely,
Bob'''
print(spam.split('\n'))

print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))

print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))
