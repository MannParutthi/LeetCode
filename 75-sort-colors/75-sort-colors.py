class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         noOf0s = 0
#         noOf1s = 0
#         noOf2s = 0
        
#         for ele in nums:
#             if ele == 0:
#                 noOf0s += 1
#             elif ele == 1:
#                 noOf1s += 1
#             elif ele == 2:
#                 noOf2s += 1
            
#         index = 0
#         while index < len(nums):
#             while noOf0s != 0:
#                 nums[index] = 0
#                 index += 1
#                 noOf0s -= 1
#             while noOf1s != 0:
#                 nums[index] = 1
#                 index += 1
#                 noOf1s -= 1
#             while noOf2s != 0:
#                 nums[index] = 2
#                 index += 1
#                 noOf2s -= 1

        #Dutch national flag problem
        frontPtr = 0
        rearPtr = len(nums) - 1
        
        index = 0
        while index <= rearPtr:
            if nums[index] == 0:
                nums[index] , nums[frontPtr] = nums[frontPtr] , nums[index]
                frontPtr += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            elif nums[index] == 2:
                nums[index] , nums[rearPtr] = nums[rearPtr] , nums[index]
                rearPtr -= 1   
            
            
            