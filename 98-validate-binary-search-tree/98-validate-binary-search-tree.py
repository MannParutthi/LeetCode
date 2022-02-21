# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def valid(self, node, leftBoundary, rightBoundary):
        if not node:
            return True
        
        if not (leftBoundary < node.val < rightBoundary):
            return False

        return (self.valid(node.left, leftBoundary, node.val) and 
               self.valid(node.right, node.val, rightBoundary))
        
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))
        