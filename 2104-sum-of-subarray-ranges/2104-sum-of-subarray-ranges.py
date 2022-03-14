class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums)): # take ele & check diff with all remaining ele => num[0], num[1:] or nums[1], num[2:]
            minNo = nums[i]
            maxNo = nums[i]
            for j in range(i, len(nums)):
                minNo = min(minNo, nums[j])
                maxNo = max(maxNo, nums[j])
                res += maxNo - minNo
                
        return res