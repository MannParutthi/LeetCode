# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNumFromLinkedList(self, l: ListNode):
        num = ''
        current = l
        while current:
            num += str(current.val)
            current = current.next
        return num[::-1]
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        totalSum = int(self.getNumFromLinkedList(l1)) + int(self.getNumFromLinkedList(l2))
        totalSum = str(totalSum)[::-1]
        
        newLinkedList = ListNode(totalSum[0])
        current = newLinkedList
        i = 1
        while i <= len(totalSum)-1 :
            current.next = ListNode(totalSum[i])
            current = current.next
            i += 1
        return newLinkedList