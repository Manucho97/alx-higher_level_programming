#!/usr/bin/python3
if __name__ == "__main__":
    import sys

counter = 0
n = len(sys.argv)
if n == 1:
    print("{} arguments.".format(n - 1))
elif n == 2:
    print("{} argument:".format(n - 1))
else:
    print("{} arguments:".format(n - 1))
for i in range(1, n):
    counter += 1
    print("{}: {}".format(counter, sys.argv[i]))
