#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    numOfArg = len(argv) - 1
    if numOfArg < 1:
        print("{} arguments.".format(numOfArg))
    elif numOfArg == 1:
        print("{} argument:".format(numOfArg))
    else:
        print("{} arguments:".format(numOfArg))
    for x in range(numOfArg):
        print("{}: {}".format(x + 1, argv[x + 1]))
