from Typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        new_row = [1]
        result = self._getRow(rowIndex - 1, new_row)
        return result
        
    def _getRow(self, rowIndex: int, last_row: List[int]) -> List[int]:
        if rowIndex == -1:
            return last_row
        new_row = [1]
        
        for i in range (len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        return self._getRow(rowIndex - 1, new_row)