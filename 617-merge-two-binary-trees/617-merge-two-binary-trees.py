# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        nodeTree1 = root1
        nodeTree2 = root2
        if root1 and root2:
            root = TreeNode(nodeTree1.val + nodeTree2.val)
            root.left = self.mergeTrees(nodeTree1.left, nodeTree2.left)
            root.right = self.mergeTrees(nodeTree1.right, nodeTree2.right)
            return root
        else:
            return nodeTree1 or nodeTree2