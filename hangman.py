#This game is Hangman
#Feels like this one is going to be some great typing practice

import random
HANGMAN_PICS = ['''
		+---+
		    |
		    |
		    |
		=====''','''
		+---+
		O   |
		    |
		    |
		=====''','''
		+---+
		O   |
		|   |
		    |
		=====''','''
		+---+
		O   |
   	       /|   |
		    |
		=====''','''
		+---+
		O   |
  	       /|\  |
		    |
		=====''','''
		+---+
		O   |
	       /|\  |
	       /    |
		=====''','''
		+---+
		O   |
	       /|\  |
	       / \  |
		=====''']

words = '''ant baboon badger bad bear beaver camel cat clam cobra cougar coyote ceqo deer dog donkey duck eagle ferret
	   fox frog goat goose hawk lion lozard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon
	   python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'''.split()

def getRandomWord(wordList):
	#This function returns a random string from the passed list of strings above it
	wordIndex = random.randint(0, len(wordList)-1)
	return wordList[wordIndex]
