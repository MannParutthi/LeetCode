class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        totalMul = 1
        for i in range(len(nums)):
            answer.append(totalMul)
            totalMul *= nums[i]
        
        totalMul = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= totalMul
            totalMul *= nums[i]
        
        return answer
    
#         totalSum = 1
#         for ele in nums:
#             totalSum *= ele
        
#         answer = []
#         for index, value in enumerate(nums):
#             if value != 0:
#                 answer.append(totalSum//value)
#             else:
#                 temp = nums[:index] + nums[index+1:]
#                 tempSum = 1
#                 for ele in temp:
#                     tempSum *= ele
#                 answer.append(tempSum)
#         return answer
                