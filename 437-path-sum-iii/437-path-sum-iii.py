# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def pathSumWithNodeVal(node, remainingSum):
            if node == None: return 0
            
            res = 0
            if node.val == remainingSum:
                res += 1
                
            res += pathSumWithNodeVal(node.left, remainingSum - node.val)
            res += pathSumWithNodeVal(node.right, remainingSum - node.val)
            return res
        
        
        if root == None: return 0
        return pathSumWithNodeVal(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)