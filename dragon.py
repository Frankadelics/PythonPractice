import random 
import time

#Variables must also be declared beforehand too, keep this in mind to help remembering the function stuff too
#Functions must be declared before they can be called in Python!!!!
def displayIntro():
	print('You are in a land full of dragons. In front of you, you see two caves, the dragon is friendly')
	print('and will share his treasure with you. The other dragon is greedy and hungry, and will eat you in sight.')
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
		if cave < '1' or cave > '2':
			print('Pick a number between 1 and 2 please!')
		else:
			print()
	return  cave

def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	time.sleep(2)

	friendlyCave = random.randint(1,2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
		print()
	else:
		print('Gobbles you down in one bite!')
		print()
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	checkCave(chooseCave())
	print('Do you want to play again? (yes or no?)')
	playAgain = input()
