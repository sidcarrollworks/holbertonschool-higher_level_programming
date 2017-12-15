#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return num

    slen = len(roman_string)
    i = 0
    while i < slen:
        num1 = roman[roman_string[i]]

        if i + 1 < slen:
            num2 = roman[roman_string[i + 1]]

            if num1 >= num2:
                num += num1
                i += 1
            else:
                num += num2 - num1
                i += 2
        else:
            num += num1
            i += 1
    return num
