# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #'=' & <' not supported between instances of 'ListNode' and 'ListNode' in Python 3
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        heap = [] #heap will have (len of lists) no of value => min heap
        head = tail = ListNode(None)
        
        for linkedlist in lists: # push pointers of all linkedlist with its value in heap
            if linkedlist:
                heapq.heappush(heap, (linkedlist.val, linkedlist))
        
        while heap:  
            val, linkedlist = heapq.heappop(heap) # take out value from min heap
            tail.next = ListNode(val) # add it to result
            tail = tail.next
            if linkedlist.next: # then increment the pointer of that linkedlist and push it again to heap
                heapq.heappush(heap, (linkedlist.next.val, linkedlist.next))
        
        return head.next