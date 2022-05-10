class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left = 0
        right = len(nums)-1
        
        while left <= right:
            if nums[left] < nums[right]: # already sorted from left to right
                res = min(res, nums[left])
                break
            else:
                mid = (left+right) // 2
                res = min(res, nums[mid])
                if nums[mid] >= nums[left]: # left to mid already sorted => so go on right side (mid to right)
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return res