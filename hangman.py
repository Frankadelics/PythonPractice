#This game is Hangman
#Feels like this one is going to be some great typing practice

import random
HANGMAN_PICS = ['''
		+---+
		    |
		    |
		    |
		=====''',
		     '''
		+---+
		O   |
		    |
		    |
		=====''',
		     '''
		+---+
		O   |
		|   |
		    |
		=====''',
		     '''
		+---+
		O   |
   	       /|   |
		    |
		=====''',
		     '''
		+---+
		O   |
  	       /|\  |
		    |
		=====''',
		     '''
		+---+
		O   |
	       /|\  |
	       /    |
		=====''',
		     '''
		+---+
		O   |
	       /|\  |
	       / \  |
		=====''']

words = '''ant baboon badger'''.split()

def getRandomWord(wordList):
	#This function returns a random string from the passed list of strings above it
	wordIndex = random.randint(0, len(wordList)-1)
	return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()
	print('Missed letters:', end='')
	for letter in missedLetters:
		print(letter, end='')
	print()
	blanks = '_' * len(secretWord)

	#Replace blanks with correcftly guessed letters.
	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

	#Show the secret wword with spaces in between each letter.
	for letter in blanks:
		print(letter, end='')
	print()

#Returns the letter the plaer entered. This function makes sure the player entered a single letter and not something else
def getGuess(alreadyGuessed):
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) !=1:
			print('Please enter a single letter.')
		elif guess in alreadyGuessed:
			print('Youhave already guessed that letter. Choose again')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Pleaser enter a LETTER.')
		else:
			return guess

#This functions returns TRUE if the plaer wants to play again; otherwise, it returns FALSE
def playAgain():
	print('Do you want to play again? (yes or no)')
	return input().lower().startswith('y')

print(' H A N G M A N ')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(missedLetters, correctLetters, secretWord)

	#Let the player enter a letter.
	guess = getGuess(missedLetters + correctLetters)
	if guess in secretWord:
		correctLetters = correctLetters + guess

		#Check if the player has won.
		foundAllLetters =  True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Yes! The secret word is "' + secretWord + '"! You have WON!') 
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess

	#Check if the player has guessed too many times and lost.
	if len(missedLetters) == len(HANGMAN_PICS) - 1:
		displayBoard(missedLetters, correctLetters, secretWord)
		print('You have run out o guessess!')
		print('After' + str(len(missedLetters)) + 'missed guesses and ' + str(len(correctLetters)) + 'correct guesses, ')
		print('the word was"' +secretWord + '"')
		gameIsDone = True

#Ask if the player if they would like to play again, but only if the game is done
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord = getRandomWord(words)
		else:
			break

