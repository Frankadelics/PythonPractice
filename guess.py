#This is a game that will hopefully teach me how to use python well
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()
print()

number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')
print(myName + ', you get 6 tries before the number is revealed to you.')
print('So good luck and happy guessing.')
print()

for guessesTaken in range(6):
	chancesLeft = 6 - guessesTaken
	chancesLeft = str(chancesLeft)
	print('Take a guess. You have ' + chancesLeft + ' chances left!')
	guess = input()
	guess = int(guess)

	if guess < number:
		print('Your guess is too low.')
		print()

	if guess > number:
		print('Your guess is too high.')
		print()

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
	print()

if guess != number:
	number = str(number)
	print('Nope. The number I was thinking of was ' + number + '.')
	print()
