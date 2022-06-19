# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # Null/Empty tree is a sub-tree of all trees
        if not root: return False # root & subRoot => both null
        
        if self.isSameTree(root, subRoot):
            return True
    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
    # https://leetcode.com/problems/same-tree/
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or (p.val != q.val):
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)