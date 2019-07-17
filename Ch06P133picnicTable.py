#! /Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python

def printItems(itemsDict, leftWidth, rightWidth):
    print('ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(str(k).ljust(leftWidth, '.') + str(v).rjust(rightWidth))


def printContents(itemsDict, col1Width, col2Width):
    space = 3
    print('ITEMS'.center(col1Width + space + col2Width, '-'))
    for k, v in itemsDict.items():
        print(str(k).rjust(col1Width) + ' ' * 3 + str(v).rjust(col2Width, '.'))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printItems(picnicItems, 12, 5)
printItems(picnicItems, 20, 6)

gvbcSongBookDictionary = {
    1: 'A Common Love',
   13: 'Be Still and Know',
   29: 'Deep Down in My Heart',
   35: 'Father I Adore You',
   44: 'God Is So Good',
   58: 'He Paid a Debt',
}
printContents(gvbcSongBookDictionary, 4, 30)
