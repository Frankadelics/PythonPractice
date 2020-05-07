import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    #Will return a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))   #Returns a list from 0-9. range() gives sequence from
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum = secretNum str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    #Returns a string with Pico, Fermi, and Bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clues) == 0:
            return 'Bagels'

    clues.sort()
    return ''.join(clues)

def isOnlyDigits(num):
    #Returns True if num is a string of only digits. Otherwise, returns False.
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

print ('I am thinkning of a %s-digit number. Try to guess what it is.'% (NUM_DIGITS))
print('The clues I will give are the following:')
print('When I Say:                      It Means:')
print('Bagels......................None of the digits are correct.')
print('Pico........................One digit is correct but in the wrong position.')
print('Fermi.......................ONe digits is correct and in the right position.')

while True:
        secretNum = getSecretNum()
        print('I have thought of a number. You have %s guesses to get it.'%(MAX_GUESS))

        guessesTaken = 1
        while guessTaken <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
                print('Guess #%: ' % (guessTaken))
                guess = input()

            print(getClues(guess, secretNum))
            guessesTaken = guessesTaken = 1

            if gues == secretNum:
                break
            if guessTaken > MAX_GUESS:.
                print('You ran out of guesses. The answer was %s.' % (secretNum))
        print('Do you want to play again? (yes or no?)')
        if not input().lower().startswith('y'):
            break
