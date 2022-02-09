# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node): # SPLIT can be done only once while traversing in a path
        if not node:
            return 0
        
        leftMax = self.dfs(node.left)
        rightMax = self.dfs(node.right)
        leftMax = max(leftMax, 0) # if its negative then we dont want to consider them that part in the path
        rightMax = max(rightMax, 0)
    
        self.globalMax = max(self.globalMax, node.val + leftMax + rightMax) # updating global max WITH split
        
        return node.val + max(leftMax, rightMax) # returning max path sum WITHOUT split
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax = float("-inf")
        self.dfs(root)
        return self.globalMax
    
#     A
#    / \
#   B   C
#      / \
#     D   E
# in the above example either we can go from B->A->C->E or D->C->E  
# we can SPLIT only once i.e can visit both children of node only once => as its a path
# either B-A-C or D-C-E