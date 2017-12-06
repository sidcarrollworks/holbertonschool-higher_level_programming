#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
print("Last digit of {:d} is {:d} ".format(number, lastDigit), end="")
if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is 0")
elif number < 6 and number != 0:
    print("and is less than 6 and not 0")
