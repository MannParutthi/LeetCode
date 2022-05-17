class Solution:
    def jump(self, nums: List[int]) -> int: # dp[i] = -1 => cant be reached from index i
        dp = [-1] * len(nums) # it stores from that index how many min jumps are required to reach last index
        dp[-1] = 0 # already on last index so 0 jumps are req
        
        for i in range(len(nums)-1, -1, -1): # traverse from end to start & chk for min no of jumps req
            
            maxNoOfStepsAllowedFromI = nums[i]
            minNoOfJumpsReqFromI = float('inf')
            
            for j in range(1, maxNoOfStepsAllowedFromI+1):
                if (i+j) < len(nums) and dp[i+j] != -1 and dp[i+j] < minNoOfJumpsReqFromI:
                    minNoOfJumpsReqFromI = dp[i+j]
                    
            if minNoOfJumpsReqFromI != float('inf'):
                dp[i] = minNoOfJumpsReqFromI + 1
            
        return dp[0]
        