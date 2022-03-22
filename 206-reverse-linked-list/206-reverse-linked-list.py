# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        currentNode = head
        while currentNode is not None:
            # storing ref of next node so that it is not lost
            nextNode = currentNode.next
            
            # reversing the pointer/link
            currentNode.next = prevNode
            
            # incrementing nodes            
            prevNode = currentNode
            currentNode = nextNode
        
        # last node is stored in prevNode, so making the last node as head
        head = prevNode
        return head