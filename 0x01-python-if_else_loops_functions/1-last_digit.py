#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num1 = (number * -1)
else:
    num1 = number
num2 = num1 % 10
if number >= 0:
    if num2 > 5:
        print("Last digit of {} is {} and is greater than 5"
              .format(number, num2))
    elif num2 == 0:
        print("Last digit of {} is {} and is 0"
              .format(number, num2))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".
              format(number, num2))
else:
    num2 = num2 * -1
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, num2))
