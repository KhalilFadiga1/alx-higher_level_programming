#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for int in my_list:
            new_list.append(True if int % 2 == 0 else False)
        return new_list
