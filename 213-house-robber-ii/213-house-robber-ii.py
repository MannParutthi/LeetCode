class Solution:
    def houseRobber1(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        maxAmounAtIndex = [0] * (len(nums)+1) # it stores max amount that can be robbed till index i
        maxAmounAtIndex[0] = 0
        maxAmounAtIndex[1] = nums[0]
        
        for i in range(len(nums)):
            maxAmounAtIndex[i+1] = max(maxAmounAtIndex[i], maxAmounAtIndex[i-1]+nums[i])
        return maxAmounAtIndex[-1]
    
    def rob(self, nums: List[int]) -> int: # circle => so 1st and last cant be together
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        return max(self.houseRobber1(nums[1:]), self.houseRobber1(nums[:-1])) # skip 1st , skip last
    
        