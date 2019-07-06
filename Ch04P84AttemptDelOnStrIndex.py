# test to see if the del statement can delete a character from a string

spam = 'Phillip, the name spelled like most Americans do, has a double "l".'
print(spam)

newSpam = spam
print(newSpam)

del newSpam[4]
print(newSpam)

# Result:
# Phillip, the name spelled like most Americans do, has a double "l".
# Phillip, the name spelled like most Americans do, has a double "l".
# Traceback (most recent call last):
#   File "/Volumes/javaDisk/PyNoStarch/AutomateTheBoringStuff/tryDelOnStrIndexCh4P84.py", line 9, in <module>
#     del newSpam[4]
# TypeError: 'str' object doesn't support item deletion