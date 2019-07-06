# -*- coding: utf-8 -*-
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Input is guaranteed to be within the range from 1 to 3999.
"""
# не работает пока на всех примерах, т.к. 6!=720, а этот способ дико неоптимален)

def convert_ri(key):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    d11 = key.find('IV')
    d12 = key.find('IX')
    d21 = key.find('XL')
    d22 = key.find('XC')
    d31 = key.find('CD')
    d32 = key.find('CM')

    if len(key) > 2:
        sum41 = 0
        for i in range(len(key)):
            sum41 += d[key[i]]
        sum41 = sum41

        if key[0] == 'I':
            return "You are Bad Guy!"
        elif d11 != -1:
            return sum41 - 2
        elif d12 != -1:
            return sum41 - 2
        elif d21 != -1:
            return sum41 - 20
        elif d22 != -1:
            return sum41 - 20
        elif d31 != -1:
            return sum41 - 200
        elif d32 != -1:
            return sum41 - 200
        else:
            return sum41

    elif len(key) > 1:
        if key == 'II':
            return 2
        elif key == 'III':
            return 3
        elif key == 'IV':
            return 4
        elif key == 'IX':
            return 9
        elif key == 'XL':
            return 40
        elif key == 'XC':
            return 90
        elif key == 'CD':
            return 400
        elif key == 'CM':
            return 900
        else:
            return sum41

    else:
        if key in d:
            return d[key]
        else:
            return "This is new shit!"


print(convert_ri(input()))