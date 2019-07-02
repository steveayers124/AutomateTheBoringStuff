# Review AutomateTheBoringStuff Chapter 4 principles, test out a few things

spam = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
bacon = [3.14, 'cat', 11, 'cat', True, 'the', 'ate', ' ']
print(len(spam))
print(len(bacon))
print(len(spam + bacon))
print(len(str(spam + bacon)))
print(str(spam + bacon))
sausage = [spam, bacon]
print(sausage)
print(sausage[1])
print(sausage[0])
print(sausage[0][0])
# a cat ate 3.14
print(sausage[0][0] + sausage[1][7] + sausage[1][3] + sausage[1][7] + sausage[1][bacon.index("ate")] + sausage[1][7] + str(sausage[1][0]))

egg = [
    ['elephant ','bat ',         'cat ',     'mouse '], 
    ['is ',      'is afraid of ','ate '], 
    ['fuschia ', 'maddened ',    'of doom ', 'flying '], 
    ['a ',       'an ',          'the ',     'of ',      'to ',    ' ']
    ]
# the fuschia bat of doom ate the maddened flying mouse 
# the cat of doom ate the flying mouse of doom 
# the elephant is afraid of the maddened fuschia bat 
# the bat is a flying mouse 
print(egg[3][2] + egg[2][0] + egg[0][1] + egg[2][2] + egg[1][2] + egg[3][2] + egg[2][1] + egg[2][3] + egg[0][3])
print(egg[3][2] + egg[0][2] + egg[2][2] + egg[1][2] + egg[3][2] + egg[2][3] + egg[0][3] + egg[2][2])
print(egg[3][2] + egg[0][0] + egg[1][1] + egg[3][2] + egg[2][1] + egg[2][0] + egg[0][1])
print(egg[-1][2] + egg[0][-3] + egg[-3][-3] + egg[3][0] + egg[-2][-1] + egg[0][-1])
# print(egg[3][2] + egg[][] + egg[][] + egg[][] + egg[][] + egg[][])
# "a doom is upon me"
print(egg)
print(egg[1][1][3])
print(egg[-2][-2][-5:-1])
print(egg[1][0])
print(egg[-4][-1][2:3] + egg[-4][-4][-6:-5] + egg[-1][-2][0:2][-1] + egg[0][0][-3])
print((egg[0][3][0:1] + egg[0][0][0])[0:])

print('The ' + egg[0][-1] + 'loudly proclaimed, "' + (egg[2][2][3:]) * 3 + '!"')
