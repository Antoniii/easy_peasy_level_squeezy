# -*- coding: utf-8 -*-
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def three_sum(nums):
    result =[]
    for i in nums:
        for j in nums[1:]:
            for k in nums[2:]:
                if i + j + k == 0 and (i <= j < k or i < j <= k):
                    result.append([i,j,k])
                else:
                    None
    if len(result) == 0:
        print("This list have no one triplets!")
    else:
        return result

def filter_dublicate(list_triplets):
    pure = []
    for i in list_triplets:
        if i not in pure:
            pure.append(i)
    print(pure)

#print(three_sum([1, 2, 3, 4, 5, 6]))
#print(three_sum([-1, 0, 1, 2, -1, -4]))

filter_dublicate(three_sum([-1, 0, 1, 2, -1, -4]))
