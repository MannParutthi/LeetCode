class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, value in enumerate(nums):
            for i in range(index+1, len(nums)):
                if value + nums[i] == target:
                    return [index, i]