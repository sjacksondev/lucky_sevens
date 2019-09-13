"""
Author: Sabrina
Date: 9/13/19
"""

import random

while True:
	dicePot = int(input("Enter the amount you would like to bet >> "))
	dice1 = random.randint(1,7)
	dice2 = random.randint(1,7)
	dicePair = (dice1 + dice2)
	
	if dicePair == 7 and dicePot > 0:
		print()
		print("Your first dice roll is " + str(dice1) + ".")
		print("Your second dice roll is " + str(dice2) + ".")
		print("Yeah! You won $4! Your new pot is" + " $" + str(dicePot + 4) + "!" + " Let's play again!")
	elif dicePot > 0:
		print()
		print("Your first dice roll is " + str(dice1) + ".")
		print("Your second dice roll is " + str(dice2) + ".")
		print("Da da daaaaaa! You loss $1! Your new pot is now" + " $" + str(dicePot - 1) + "!" + " Let's play again!")
	else:
		print()
		print("Womp! Womp! Womp! You have no more money available to bet. Thanks for playing!")
		break

