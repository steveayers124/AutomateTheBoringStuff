# Guess the number game
import random

lowerLimit = 1
upperLimit = 10
secretNumber = random.randint(lowerLimit, upperLimit)
# Secretly reveal the answer to yourself, hidden from others...
print('/Volumes/javaDisk/PyNoStarch/AutomateTheBoringStuff/Ch' + str(secretNumber) + 'p74.py')
print('I\'m thinkin\' of a number between ' + str(lowerLimit) + ' and ' + str(upperLimit) + '.')
print('Take a few guesses.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 4):
    print('Wha\'d\'ya think?')
    guess = int(input())

    if guess < secretNumber:
        print(str(guess) + '? But tha\'ll be too low.')
    elif guess > secretNumber:
        print(str(guess) + '? But tha\'ll be too high.')
    else:
        break   # the condition must be the correct guess

if guess == secretNumber:
    print('Ya did good. It took ya ' + str(guessesTaken) + ' guesses.')
else:
    print('So close! ' + str(secretNumber))
