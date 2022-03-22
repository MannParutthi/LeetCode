# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        # Phase-1 : reach node at "left" position
        leftPrev = dummy
        curr = head
        for i in range(left-1):
            leftPrev = curr
            curr = curr.next
        # Now curr = "left" & leftPrev = "node before left"
        
        # Phase-2 : Reverse from "left" to "right"
        prev = None
        for i in range(right - left + 1):
            tempCurrNext = curr.next
            curr.next = prev
            
            prev = curr
            curr = tempCurrNext
        
        # Phase-3 : Update pointers
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        return dummy.next