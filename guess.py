#This is a game that will hopefully teach me how to use python well
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
print(myName + ' you get 6 tries before the number is revealed to you')
print('So good luck and happy guessing')

for guessesTaken in range(6):
	print('Take a guess.')
	guess = input()
	guess = int(guess)
	chancesLeft = 5 - guessesTaken
	chancesLeft = str(chancesLeft)

	if guess < number:
#		chancesLeft = str(chancesLeft)
		print('Your guess is too low.')
		print('You only have ' + chancesLeft + ' more tries left!')

	if guess > number:
#		chancesLeft = str(chancesLeft)
		print('Your guess is too high.')
		print('You only have ' + chancesLeft + ' more tries left!')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Goof job, ' + myName + '! You guessed my number in ' + guessesTaken + 'guesses!')

if guess != number:
	number = str(number)
	print('Nope. The number I was thinking of was ' + number + '.')
