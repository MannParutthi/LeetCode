class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMapStoringPrevEles = {}
        
        for i, val in enumerate(nums):
            remVal = target-val 
            if remVal in hashMapStoringPrevEles:
                return [i, hashMapStoringPrevEles[remVal]]
            else:
                hashMapStoringPrevEles[val] = i