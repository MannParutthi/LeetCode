# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # def traverse()
    
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        
        queue = []
        queue.append(root)
        
        levelNo = 0
        while queue:
            currLevel = []
            size = len(queue)
            
            for i in range(size):
                currNode = queue.pop(0)
                if currNode.left is not None:
                    queue.append(currNode.left)
                if currNode.right is not None:
                    queue.append(currNode.right)
                currLevel.append(currNode.val)
            if levelNo%2 != 0: res.append(currLevel[::-1])
            else: res.append(currLevel)
            levelNo += 1
        
        return res
        