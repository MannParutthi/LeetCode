# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0]
        
        def dfs(node): # returns height of a node
            if not node:
                return -1 # height of node with no child
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            maxDiameter[0] = max(maxDiameter[0], leftHeight+1 + rightHeight+1)
            
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return maxDiameter[0]