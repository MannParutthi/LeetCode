"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        oldToNewHashMap = {} # will store corresponding cloned node of the original
        
        def dfs(node):
            if node in oldToNewHashMap: # if copy exists - return it
                return oldToNewHashMap[node]
            
            copy = Node(node.val) # else - make a copy
            oldToNewHashMap[node] = copy
            
            for neighbor in node.neighbors: # make copy of all neighbors
                copy.neighbors.append(dfs(neighbor)) # and add them (cloned ones) to the neighbors list
            return copy
        
        return dfs(node)