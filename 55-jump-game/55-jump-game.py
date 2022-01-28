class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPtrIndexPosition = len(nums) - 1
        for i in range(len(nums)-1, -1, -1): # from end try to reach start
            if i + nums[i] >= lastPtrIndexPosition: # index + maxJumpCount which can reach to or beyond the last position
                lastPtrIndexPosition = i # we just need to reach to this new index
        return lastPtrIndexPosition == 0