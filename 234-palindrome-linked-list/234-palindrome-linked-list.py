# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.leftPtr = head
        
        # helper function
        def isPalindromeHelper(rightPtr):
            if rightPtr == None:
                return True
            res = isPalindromeHelper(rightPtr.next) # rightPtr goes till end of linkedlist as its recursion 
            if res == False: return False
            elif self.leftPtr.val != rightPtr.val: return False  # while coming back it compares value of left and right ptr
            else:
                self.leftPtr = self.leftPtr.next
                return True  
        # end of helper function
        
        return isPalindromeHelper(head)
        