# -*- coding: utf-8 -*-
"""
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
"""

def my_power(x,n):
    res = 1.
    for i in range(abs(n)):
        if n > 0:
            res *= x
        elif n < 0:
            res *= 1/x
        else:
            return res
    return res

print(my_power(2,10))
print(my_power(2.1,3))
print(my_power(2,-3))
print(my_power(-2,0))
print(my_power(0,0))