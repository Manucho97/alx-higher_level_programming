#!/usr/bin/python3

x = 1
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz Buzz ", end="")
    elif x % 3 == 0:
        print("Fizz ", end='')
    elif x % 5 == 0:
        print("Buzz ", end='')
    else:
        print(f"{x} ", end='')
    x += 1
print()