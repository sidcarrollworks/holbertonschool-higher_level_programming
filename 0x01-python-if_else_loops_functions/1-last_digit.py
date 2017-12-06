#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tmp = ""
if number < 0:
    tmp = -number
lastDigit = tmp % 10
if number < 0:
    lastDigit = -lastDigit
print("Last digit of {:d} is {:d} ".format(number, lastDigit), end="")
if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
