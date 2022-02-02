# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if not node: return None
        if p == node or q == node:
            return node
        left = self.lowestCommonAncestor(node.left, p , q)
        right = self.lowestCommonAncestor(node.right, p , q)
        
        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
        else:
            return None
    