# example using a list
import random

def printNames(names):
    for name in names:
        print('  ' + name)

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames += [name] # list concatenation
print('The cat names are:')
printNames(catNames)

if catNames != []:
    catToRemove = random.randint(0, len(catNames))
    print('\n  After some years pass, your cat ' + catNames[catToRemove] + ' passes quietly in its sleep.')
    del catNames[catToRemove]

print('Now the cat names are:')
printNames(catNames)