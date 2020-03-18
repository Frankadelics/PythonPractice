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
		=====''',
		     '''
		+---+
	       [O   |
	       /|\  |
	       / \  |
	 	=====''',
		     '''
	        +---+
	       [O]  |
 	       /|\  |
	       / \  |
	        =====''']

words = {'Colors': 'red orange yellow green blue purple'.split(),
	 'Shapes': 'square triangle rectangle circle'.split(),
	 'Fruits': 'apple orange lemon lime pear'.split(),
	 'Animals':'ant bear frog turtle'.split()}

def getRandomWord(wordDict):
	#Here I am choosing a random key from the passed word
	wordKey = random.choice(list(wordDict.keys()))

	#Here I am choosing a random item from the random key I selected above
	#Assuming wordKey = 'Animal' then  we can rewrite as
	#word[Animal] and pick randomly from 0 to N-1
	#N is the length within the list of the key
	wordIndex = random.randint(0, len(wordDict[wordKey])-1)

	return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()
	print('Missed letters:', end='')
	for letter in missedLetters:
		print(letter, end='')
	print()
	blanks = '_' * len(secretWord)

	#Replace blanks with correctly guessed letters.
	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

	#Show the secret word with spaces in between each letter.
	for letter in blanks:
		print(letter, end='')
	print()

#Returns the letter the player entered. This function makes sure the player entered a single letter and not something else
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

difficulty = 'X'
while difficulty not in ['E', 'M', 'H']:
	print('Enter difficulty: E - Easy M - Medium H - Hard')
	difficulty = input().upper()
if difficulty == 'M':
	del HANGMAN_PICS[8]
	del HANGMAN_PICS[7]
if difficulty == 'H':
	del HANGMAN_PICS[8]
	del HANGMAN_PICS[7]
	del HANGMAN_PICS[5]
	del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet  = getRandomWord(words)
gameIsDone = False

while True:
	print('The secret word is in the set: ' + secretSet)
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
			secretWord, secretSet = getRandomWord(words)
		else:
			break

