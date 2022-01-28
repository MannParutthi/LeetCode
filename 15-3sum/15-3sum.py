class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # duplicate not allowed
                continue
            
            leftPtr = i+1
            rightPtr = len(nums)-1
            while leftPtr < rightPtr:
                threeSum = a + nums[leftPtr] + nums[rightPtr] # a + b + c
                if threeSum > 0:
                    rightPtr -= 1  # decrement right ptr as arr is sorted and sum > target so we need to decrease the sum
                elif threeSum < 0:
                    leftPtr += 1  # increment left ptr as arr is sorted and sum < target so we need to increase the sum
                else:
                    res.append([a , nums[leftPtr] , nums[rightPtr]])
                    leftPtr += 1 # if we keep leftPtr as same then a + b + c = 0 => a + b = -c => it will result in duplicate answer 
                    while nums[leftPtr] == nums[leftPtr-1] and leftPtr < rightPtr: # duplicate not allowed
                        leftPtr += 1
        return res