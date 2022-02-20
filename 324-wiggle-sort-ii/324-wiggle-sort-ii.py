class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            tempArr = sorted(nums)  
            j = len(nums)-1 # take j ptr at biggest value
            i = 1 
        
            while j >= 0: # j will go from biggest value to smallest value end to start in sorted arr
                nums[i] = tempArr[j] 
                j -= 1 # filling odd positions with biggest values (j = end to mid)
                i += 2 # and then even positions with small values (j = mid to start)
            
                if i >= len(nums):
                    i = 0
                    