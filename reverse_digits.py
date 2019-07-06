# -*- coding: utf-8 -*-
"""
Example 1:

Input: 123
Output: 321


Example 2:

Input: -123
Output: -321


Example 3:

Input: 120
Output: 21
"""

def sign_reverse_digits(number):
    if number < 0:
        number = -number
        number = reverse_digits(number)
        number = -number
    else:
        number = reverse_digits(number)
    return number

def reverse_digits(number):
    if number >= 2**31-1 or number <= -2**31:
        return 0
    else:
        word = str(number)
        word = word[::-1]
        number = int(word)
    return number


#print(-2**31+2)
#print(sign_reverse_digits(-2**31+2))
#print(sign_reverse_digits(-120))
