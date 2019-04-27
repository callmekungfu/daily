"""
    Name: Remove Element
    Source: LeetCode - 27
    Link: https://leetcode.com/problems/remove-element/
    Description: Given an array nums and a value val, 
                 remove all instances of that value in-place and return the new length.
                 Do not allocate extra space for another array, 
                 you must do this by modifying the input array in-place with O(1) extra memory.
                 The order of elements can be changed. 
                 It doesn't matter what you leave beyond the new length.
"""
from typing import List

# Naive Solution
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
    print(nums)

    return len(nums)

removeElement([], 2)