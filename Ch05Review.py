# Review AutomateTheBoringStuff Chapter 5 principles, test out a few things
# dictionary data type create replace update delete search and transformation

spam = ['cats', 'dogs', 'moose', ]
bacon = ['dogs', 'moose', 'cats', ]
print(spam == bacon)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8', }
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie', }
print(eggs == ham)
print(eggs)
print(ham)

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', }
while True:
    print('Enter a name: (blank to quit)')
    # name = input()
    name = 'Alice'
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        bday = input('What is their birthday?')
        birthdays[name] = bday
        print('Birthday data updated.')
    break
print(birthdays)

spam = {'color': 'red', 'age': 42}
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

spam = {'name': 'Zophie', 'age': '7'}
print('name' in spam.keys())
print('Zophie' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)
print('age' in spam)

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)
allMyCats = []
allMyCats += [{'name': 'Pooka', 'age': 5}]
allMyCats += [{'name': 'Zophie', 'age': 7}]
allMyCats += [{'name': 'Simon', 'age': 9}]
allMyCats += [{'name': 'Lady Macbeth', 'age': 11}]
allMyCats += [{'name': 'Fat-tail', 'age': 3}]
allMyCats += [{'name': 'Miss Cleo', 'age': 1}]
print(allMyCats)

allMyCats[0]['color'] = 'black'
allMyCats[2]['color'] = 'orange tabby'
allMyCats[5]['color'] = 'tortoise'
print(allMyCats)
for cat in allMyCats:
    change = cat.setdefault('color', 'white')
    if change != 'white':
        print('Color unchanged for ' + cat.get('name') + '.  Color remains ' + cat['color'] + '.')
print(allMyCats)

spam.setdefault('color', 'white')

# page 118
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}
             }

def totalBrought(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought += v.get(item,0)
    return numBrought


print('Number of things being brought:')
print(' - Apples             ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups               ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes              ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches     ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies         ' + str(totalBrought(allGuests, 'apple pies')))
