#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [dic[key] for key in roman_string] + [0]
    result = 0
    for idx in range(len(num) -1):
        if num[idx] >= num[idx + 1]:
            result += num[idx]
        else:
            result -= num[idx]
    return result
