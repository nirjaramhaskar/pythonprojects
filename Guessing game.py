#LEVEL 2: TASK 1: Guessing Game

import random
import math
#as lower limit is 1 and higher is 100
lower=1 
higher=100

#generating random number using random method
i = random.randint(lower, higher)


# randomly instructing number of chances player can take
trial=7
print("\n    You have ",trial," chances to guess the integer!\n")
print("\n\t Let's play!!! ")
#initialising variable for counting number of trials by user
count = 0
while count < 8: #counting
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
