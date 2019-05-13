from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr) 
        max_sum = self.maxSubArraySum(arr, 0, n-1) 
        print("Maximum contiguous sum is ", max_sum) 

    def maxSubArraySum(self, arr, l, h): 
        if (l == h): 
            return arr[l] 
        m = (l + h) // 2
        return max(self.maxSubArraySum(arr, l, m), 
                self.maxSubArraySum(arr, m+1, h), 
                self.maxCrossingSum(arr, l, m, h))

    def maxCrossingSum(self, arr, l, m, h):
        sm = 0; left_sum = -10000
        for i in range(m, l-1, -1) : 
            sm = sm + arr[i] 
            
            if (sm > left_sum) : 
                left_sum = sm 
        
        sm = 0; right_sum = -1000
        for i in range(m + 1, h + 1): 
            sm = sm + arr[i] 
            
            if (sm > right_sum): 
                right_sum = sm 
        
    
        return left_sum + right_sum

solution = Solution()

solution.maxSubArray([2, 3, 4, 5, 7])