class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1: # odd sum cant be partitioned into two subsets
            return False
        
        dp = set() # it stores all possible sum combinations
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums)):
            nextDP = set()
            for val in dp:
                nextDP.add(val + nums[i])
                nextDP.add(val)
            dp = nextDP
            
        if target in dp:
            return True
        else:
            return False
