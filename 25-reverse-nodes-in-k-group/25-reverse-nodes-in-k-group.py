# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy # 1-2-3  ==> 1-3-2   here 1 is groupPrev which helped us to link 3 to it
        
        while True:
            kth = self.getKthNode(groupPrev, k) # we start from groupPrev to count k nodes => 0 to k
            if kth is None:
                break
            groupNext = kth.next
            
            # reverse group
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                
                prev = curr
                curr = temp
            
            temp = groupPrev.next # groupPrev.next = first node in group
            groupPrev.next = kth # kth node = last node in group
            groupPrev = temp
            
        return dummy.next
        