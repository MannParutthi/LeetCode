class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: 
        # our answer will be in the range of 1 to len(arr)+1 => smallest positive integer
        
        # set all negative values as 0
        for i in range(len(nums)):
            if nums[i] < 0: 
                nums[i] = 0
        
        # we go to all no and make value at that index(no) negative if its not already negative => [3,1,4,2] perfect scenario
        for n in nums:
            index = abs(n) - 1
            if index >= 0 and index < len(nums):
                if nums[index] == 0: 
                    nums[index] = float('-inf')
                elif nums[index] > 0: # we dont want to make negative to be positive again, when its duplicated num
                    nums[index] *= -1
        
        # now at index which we have negative value => means those index values exists in array
        
        # if at any index positive number exists then return value of that index as it is not in array
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
            
        return len(nums)+1 # as all numbers from 1 to len(nums) exists