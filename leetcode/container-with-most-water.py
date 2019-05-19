from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Find Tallest Wall
        tallest = max(height)
        tallest_index = height.index(tallest)
        # Find Second Tallest Wall, divide into two ways
        height_left = height[0 : tallest_index]
        height_right = height[tallest_index + 1 : -1]
        tallest_left = max(height_left)
        tallest_right = max(height_right)
        print(tallest, tallest_index, height_left, height_right)

solution = Solution()
print('hello')
solution.maxArea([1,8,6,2,5,4,8,3,7])
