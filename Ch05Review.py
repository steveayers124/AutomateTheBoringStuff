# Review AutomateTheBoringStuff Chapter 5 principles, test out a few things
# dictionary data type create replace update delete search and transformation

spam = ['cats', 'dogs', 'moose', ]
bacon = ['dogs', 'moose', 'cats', ]
print(spam == bacon)

eggs = {'name':'Zophie', 'species':'cat', 'age':'8', }
ham =  {'species':'cat', 'age':'8', 'name':'Zophie', }
print(eggs == ham)
print(eggs)
print(ham)

birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4', }
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
    
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         bday = input('What is their birthday?')
#         birthdays[name] = bday
#         print('Birthday data updated.')
print(birthdays)

spam = {'color':'red', 'age':42}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)
print(spam.keys())
print(spam.values())
print(spam.items())
for k, v in spam.items():
    print('Key: ' + str(k) + ', Value: ' + str(v))

spam = {'name':'Zophie', 'age':'7'}
print('name' in spam.keys())
print('Zophie' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)
print('age' in spam)

