from typing import List

"""
    Naive Solution.

    Time: O(n^2)
    Space: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area: int = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, min(height[i], height[j]) * (j - i))
        return max_area
    
    def maxAreaBetter(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return max_area

solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])
