# Given a list like ['apples', 'bananas', 'tofu', 'cats']
# print a corresponding string, comma separated, with "and" before the last item
# like "apples, bananas, tofu, and cats"

def commaCode(beginList):
    endString = ''
    if len(beginList) == 0:
        endString = ''
    elif len(beginList) == 1:
        endString = str(beginList[0])
    elif len(beginList) == 2:
        endString = str(beginList[0]) + ' and ' + str(beginList[1])
    else:
        for i in beginList[0:len(beginList) - 1]:
            endString += i + ', '
        endString += 'and ' + beginList[len(beginList) - 1]
    return endString

print(commaCode([]))
print(commaCode(['1oneItem']))
print(commaCode(['1twoItems', '2twoItems']))
print(commaCode(['1threeItems', '2threeItems', '3threeItems']))
print(commaCode(['1fourItems', '2fourItems', '3fourItems', '4fourItems']))

print('A few of my favorite things are ' + commaCode([
    'raindrops on roses', 
    'whiskers on kittens', 
    'bright copper kettles', 
    'warm woolen mittens',
    'brown paper packages tied up with string', 
    'cream colored ponies', 
    'crisp apple strudel',
    'doorbells', 
    'sleigh bells', 
    'schnitzel with noodles',
    'wild geese that fly with the moon on their wings',
    'dogs that bite', 
    'bees that sting', 
    'feeling sad'
]) + '.')
