#!/usr/bin/python3
def safe_print_list_integers(my_list = [], x = 0):
    calc = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end = '')
            calc += 1
        except (ValueError, TypeError):
            pass
    print()
    return calc
