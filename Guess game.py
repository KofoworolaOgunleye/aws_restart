#Guess game
import random
random_number = int(random.randint(1, 50))
name = input("Hello!, What is your name? ")
print('Hi {}!,Welcome to the game of guesses.'.format(name))

guessedNumber=input("Guess a number between 1 and 50. ")
try:
	if int(guessedNumber) < 1 or int(guessedNumber) > 50:
		raise ValueError("Guess a number between 1 and 50.")

	if int(guessedNumber) == random_number:
		print('Congratulations!, You guesed right {0} and {1} are the same'.format(guessedNumber,random_number))

	else:
		print('Oh-O!, You guessed wrong, the right number is {0}.'.format(random_number))
			
except ValueError as errorMsg:
    print("Oh no!, that is outside the given range. Please try again.")
    print("{}".format(errorMsg))
