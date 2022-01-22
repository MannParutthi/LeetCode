class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increasingSubSeqCount = [0] * len(nums) # stores count of longest sub seq ending at each element
        
        for i in range(len(nums)):
            maxSubSeq = 0
            for ptr in range(0, i): #compare with all prev value's (which are small) longest sub seq count
                if nums[i] > nums[ptr]:
                    maxSubSeq = max(maxSubSeq, increasingSubSeqCount[ptr])
            increasingSubSeqCount[i] = maxSubSeq + 1 # added for for itself / curr value
            
        return max(increasingSubSeqCount)