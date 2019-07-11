import pprint

stuff = {}


def displayInventory(inventory):
    totalItemCount = 0
    print('Inventory:')
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        totalItemCount += v
    print('Total number of items: ' + str(totalItemCount))

def addToInventory(inventory, itemList):
    for v in itemList:
        inventory.setdefault(v, 0)
        inventory[v] += 1


displayInventory(stuff)

print('Some time goes by. You are older and wiser, more experienced than before.')
print('You have gained money, and have purchased some things, found some, and been given others.')
stuff.setdefault('arrow', 12)
stuff.setdefault('gold coin', 42)
stuff.setdefault('rope', 1)
stuff.setdefault('torch', 6)
stuff.setdefault('dagger', 1)
displayInventory(stuff)

dragonBooty = ['gold coin', 'bow +1 of speedy winds', 'gold coin', 'gold coin', 'boots of stern stance']
print('You\'ve conquered a dragon! You find:')
pprint.pprint(dragonBooty)
print('')
addToInventory(stuff, dragonBooty)
displayInventory(stuff)
