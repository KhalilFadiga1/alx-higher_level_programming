#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv 
    numOfArg = len(argv) - 1
    if numOfArg == 0:
        print("0 arguments.")
    elif numOfArg == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(numOfArg))
    for x in range(numOfArg):
        print("{:d} : {:s}".format(x + 1, sys.argv[x + 1]))

