#LEVEL 2: TASK 1: Number Guesser

import random
import math
#accepting lower limit and higher limit
lower=int(input("Enter the lower limit : "))
higher=int(input("Enter the higher limit : "))

#generating random number using random method
i = random.randint(lower, higher)


# randomly instructing number of chances player can take
trial=random.randint(3, 10)
print("\n    You have ",trial," chances to guess the integer!\n")
print("\n\t Let's play!!! ")
#initialising variable for counting number of trials by user
count = 0
while count < trial: #counting
	count += 1

#taking input by player as a guess	
	guess = int(input("Guess any number = "))

#conditions for winning and losing
	if i == guess:
		print("Congrats you guess it correctly in ",
	count, " try")
		break
	elif i > guess:
		print("You guessed too small!")
	elif i < guess:
		print("You Guessed too high!")

#if lose
if count >= trial:
	print("\nThe number is %d" % i)
	print("\tTry again!")