# discover whether my answers to the Chapter 4 Practice Questions were right

# 1. [] is the empty list.
spam=[]
print(spam)
# 2. 
spam = [2,4,6,8,10]
spam[2]='hello'
print(spam)

spam = ['a','b','c','d']
# 3. 
print(spam[int(int('3' * 2) // 11)])
# 4. 
print(spam[-1])
# 5. 
print(spam[:2])

bacon = [3.14, 'cat', 11, 'cat', True]
# 6. 
print(bacon.index('cat'))
# 7. 
bacon.append(99)
print(bacon)
#8.
bacon.remove('cat')
print(bacon)

#9.
eggs=bacon+spam
print(eggs)
eggs=bacon*7
print(eggs)
#11.
eggs=spam
print(eggs)
del eggs[0]
print(eggs)
eggs.remove('c')
print(eggs)

#14.
sausage=(42,)
print(sausage)
print(list(sausage))
print(tuple(eggs))
wurst=()
print(wurst)
