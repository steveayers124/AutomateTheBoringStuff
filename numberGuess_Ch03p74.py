# Guess the number game
import random

lowerLimit = 1
upperLimit = 20
number = random.randint(lowerLimit, upperLimit)
guesses = 0
inputGuess = None

thinkingOfANumber = 'I am thinking of a number between ' + str(lowerLimit) + ' and ' + str(upperLimit) + '.'
guessTooHigh = 'Your guess is too high.'
guessTooLow = 'Your guess is too low.'
takeAGuess = 'Take a guess.'
youGuessed = 'Good job! You guessed my number in '

# Secretly reveal the answer to yourself, hidden from others...
print('/Volumes/javaDisk/PyNoStarch/AutomateTheBoringStuff/Ch' + str(number) + 'p74.py')
print(thinkingOfANumber)
while inputGuess != number:
    print(takeAGuess)
    inputGuess = int(input())
    guesses += 1
    if inputGuess < number:
        print(guessTooLow)
    elif inputGuess > number:
        print(guessTooHigh)

if guesses == 1:
    inGuesses = ' guess!'
else:
    inGuesses = ' guesses!'

print(youGuessed + str(guesses) + inGuesses)
