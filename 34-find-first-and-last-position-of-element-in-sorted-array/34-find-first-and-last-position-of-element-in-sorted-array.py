class Solution:
    def binarySearchForFirstIndex(self, nums, target, low, high):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else: # target == mid
                res = mid
                high = mid-1 # we'll go left side to check left most matching ele i.e first ele of value target 
        return res
    
    def binarySearchForLastIndex(self, nums, target, low, high):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
            else: # target == mid
                res = mid
                low = mid+1 # we'll go right side to check right most matching ele i.e last ele of value target 
        return res
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        
        result[0] = self.binarySearchForFirstIndex(nums, target, 0, len(nums)-1)
        result[1] = self.binarySearchForLastIndex(nums, target, 0, len(nums)-1)
        
        return result