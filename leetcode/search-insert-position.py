from typing import List
"""
    Name: Search Insert Position
    Difficulty: EASY
    URL: https://leetcode.com/problems/search-insert-position/
"""
# Naive
# Runtime: 40 ms, faster than 51.73% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.6 MB, less than 5.11% of Python3 online submissions for Search Insert Position.
def searchInsert(nums: List[int], target: int) -> int:
    for i in range(0, len(nums)):
        if (target <= nums[i]):
            return i
    return len(nums)
        
print(searchInsert([1],0))