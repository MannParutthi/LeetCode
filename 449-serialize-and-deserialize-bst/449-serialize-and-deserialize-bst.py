# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return 'x'
        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)]) 
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        dataArr = data.split(",")
        return self.deserializeHelper(dataArr)
    
    def deserializeHelper(self, dataArr):
        if dataArr[0] == 'x': 
            dataArr.pop(0)
            return None
        
        node = TreeNode(dataArr.pop(0))
        node.left = self.deserializeHelper(dataArr)
        node.right = self.deserializeHelper(dataArr)
        return node
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans