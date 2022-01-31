# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        for i in range(n): # fast ptr will be n distance from slow ptr
            fast = fast.next
        
        if fast == None: # This situation would happen when we are required to del the first node (n = len(List))
            return slow.next # Also, it can handle the [] case
            
        # fast ptr will keep the distance of n from slow ptr
        while fast.next != None: # when fast reaches the last ele then slow will be at (n-1)th index/node from end
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next # removing node/ele
        
        return head
        
        