class Solution:
    def modifiedBinarySearch(self, nums, target, low, high):
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] == target:
                return mid        
            
            if nums[low] <= nums[mid]: # Left part is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else: # Right part is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return -1 # Not found

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: 
            return -1
        
        return self.modifiedBinarySearch(nums, target, 0, len(nums)-1)