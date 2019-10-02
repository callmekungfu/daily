#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if (len(digits) == 0):
            return []
        lm = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ac = ['']
        perm = []
        for digit in digits:
            current = []
            for letter in lm[digit]:
                for combination in ac:
                    current.append(combination + letter)
            ac = current
        return ac
            
        
# @lc code=end

