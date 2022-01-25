class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        
        i = float('inf') # will store 1st smallest ele => for a < b < c => it stores 'a'
        j = float('inf') # will store 2nd smallest ele => for a < b < c => it stores 'b'

        for index in range(len(nums)):
            if nums[index] <= i:
                i = nums[index]
            elif nums[index] <= j: # control will come here only when we have found i < nums[index]  
                j = nums[index]
            else: # control will come here only when we have found 2 elements i & j in increasing order i < j and i < j < nums[index]
                return True

        return False