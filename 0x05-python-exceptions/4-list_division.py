#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotient_list = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            quotient_list.append(div)
    return quotient_list
