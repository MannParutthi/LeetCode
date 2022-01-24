# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddleEleInLinkedList(self, head): # returns middle element of linked list
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseLinkedList(self, node): # returns last node after reversing
        prevNode = None
        currNode = node
        while currNode != None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None: return True
        
        mid = self.findMiddleEleInLinkedList(head)
        last = self.reverseLinkedList(mid)

        curr = head
        while curr != None and last != None:
            if curr.val != last.val: 
                return False
            curr = curr.next
            last = last.next
            
        return True
        
        
#         self.leftPtr = head
#         # helper function
#         def isPalindromeHelper(rightPtr):
#             if rightPtr == None:
#                 return True
#             res = isPalindromeHelper(rightPtr.next) # rightPtr goes till end of linkedlist as its recursion 
#             if res == False: return False
#             elif self.leftPtr.val != rightPtr.val: return False  # while coming back it compares value of left and right ptr
#             else:
#                 self.leftPtr = self.leftPtr.next
#                 return True  
#         # end of helper function
#         return isPalindromeHelper(head)
        