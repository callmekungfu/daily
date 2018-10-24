from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self._reverseString(s, 0)

    def _reverseString(self, s: List[str], x: int):
        if x == len(s) // 2:
            return
        start = s[x]
        end = s[-1 - x]
        s[x] = end
        s[-1 - x] = start
        self._reverseString(s, x + 1)
        
        