'''
    Validate Binary Search Tree
    https://leetcode.com/problems/validate-binary-search-tree/submissions/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        return self._isValidBSTLeft(root, INT_MIN, INT_MAX)
        
        
    def _isValidBSTLeft(self, node: TreeNode, lb: int, ub: int):
        if node is None: 
            return True
        if (node.val >= ub or node.val <= lb):
            return False
        return self._isValidBSTLeft(node.left, lb, node.val) and self._isValidBSTLeft(node.right, node.val, ub)