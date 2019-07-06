# -*- coding: utf-8 -*-
"""
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def two_sum(listN, target):
    result = []
    for i in range(len(listN)):
        for j in range(len(listN)):
            if listN[i] + listN[j] == target:
                if i < j:
                    result.append([i,j])                
            else:
                None
    return result

print(two_sum([2, 7, 11, 15, 47, 14, -6, 3, 23, -2], 9))
