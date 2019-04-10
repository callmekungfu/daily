class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i in range(0, len(nums)):
            map[nums[i]] = i
        for i in range(0, len(nums)):
            compliment = target - nums[i]
            if (compliment in map and map[compliment] != i):
                return [i, map[compliment]]
        raise ValueError('No solutions avaliable')
