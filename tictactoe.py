#Gonna make tic tac toe with Python this time around

import random

def drawBoard(board):
	#This function prints out the board that it waas passed

	#"board" is a list of 10 strings representing the board (ignore index 0).
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
	#This asks the player what letter they want to be
	#A list is returned, the player's letter is the first and the computer is the second
	letter = ''
	while not (leter == 'X' or leter == 'O'):
		print('Do you wanto be X or O?')
		leter = input().upper()

	#The first element in the list is the player's letter' the second is the computer's letter
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	#Randomly choose which player goes first.
	if random.randint(0,1) == 0:
		return 'computer'
	else
		return 'player'

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	#Given a board and a player's letter, this function returns True if that player has won
	#"Bo" is  board and "le" is letter so we don't type all that much
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or #Across the top
		(bo[4] == le and bo[5] == le and bo[6] == le) or #Across the middle
		(bo[1] == le and bo[2] == le and bo[3] == le) or #Across the bottom
		(bo[7] == le and bo[4] == le and bo[1] == le) or #Down the left side
		(bo[8] == le and bo[5] == le and bo[2] == le) or #Down the middle
		(bo[9] == le and bo[6] == le and bo[3] == le) or #Down the right side
		(bo[7] == le and bo[5] == le and bo[3] == le) or #Diagonal
		(bo[9] == le and bo[5] == le and bo[1] == le))   #Diagonal
