class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        kIndex = len(nums) - k
        nums[:] = nums[kIndex:] + nums[:kIndex]
