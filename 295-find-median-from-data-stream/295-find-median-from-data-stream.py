from heapq import *

class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # max heap contains all values less than X => we will take out max value from this
        self.minHeap = [] # min heap contains all value greater than X => we will take out min vale from this

    def addNum(self, num: int) -> None:
        # we will try to keep balance (equal size) between both => maxHeap can have n+1 ele and minHeap can have n ele
        # negative val cox its minHeap as by default heap in python is maxHeap
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, -num))
        else:
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, num))


    def findMedian(self) -> float:
        # if size is odd then median is value from maxHeap and if even then value from both heap and their average
        if len(self.maxHeap) == len(self.minHeap):
            return float(self.maxHeap[0] + (- self.minHeap[0])) / 2.0
        else:
            return float(self.maxHeap[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()