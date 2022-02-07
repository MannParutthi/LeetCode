class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # if we take 0/1 and all nums are negative => so we are taking max of nums 
        currMin = 1
        currMax = 1
        
        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
            else:
                prevMin = currMin
                prevMax = currMax
                currMin = min(n*prevMin, n*prevMax, n)
                currMax = max(n*prevMin, n*prevMax, n)
                res = max(res, currMax)
                
        return res