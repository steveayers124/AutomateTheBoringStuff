# given an input value to begin, print its Collatz Sequence

def collatz(number):
    remainder = number % 2
    if remainder == 0:
        try:
            result = number // 2
        except ZeroDivisionError:
            print('Error: diviision by zero')
    elif remainder == 1:
        result = (number * 3) + 1
    return result

print('\n', end='')
print('=' * 90)
print('Welcome to the Collatz Sequence Generator, the World\'s Simplist Impossible Math Problem!')
print('You enter a number, and I\'ll give the Collatz Sequence for it. This always ends in 1.')
seed = 0
while not (seed > 0):
    try:
        print('Please enter an integer greater than 0.')
        seed = int(input())
    except ValueError:
        continue
print('- ' + str(seed) + ' - ', end='')
# if seed == 1:
#     exit()
value = seed
while value != 1:
    value = collatz(value)
    print(str(value) + ' - ', end='')
print('\n' + ('=' * 90))
print('\n', end='')
