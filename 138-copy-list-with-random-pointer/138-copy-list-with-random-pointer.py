"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        
        temp = head
        randomPtrDict = {}
        while temp != None: # make a copy of all nodes of list and store them in the dictionary / hashmap
            randomPtrDict[temp] = Node(temp.val) # now dict holds all corresponding node's copy / clone  
            temp = temp.next
            
        temp = head
        while temp != None: # now connect the next and random of the cloned nodes to its corresponding nodes
            if temp.next: randomPtrDict[temp].next = randomPtrDict[temp.next]
            if temp.random: randomPtrDict[temp].random = randomPtrDict[temp.random]
            temp = temp.next
        
        return randomPtrDict[head]