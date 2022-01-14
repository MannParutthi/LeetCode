from itertools import permutations
class Solution:
    
    def backtrack(self, numsList, path, res):
        if not numsList:
            res.append(path)
            # print("after appending ==> ", numsList, path, res)
        # print()
        for i in range(len(numsList)):
            # print("numList ==> ", numsList)
            # print("index ==> ", i)
            # print("val at index ==> ", numsList[i])
            # print("numsList, path, res ==> ", numsList[:i]+numsList[i+1:] , path+[numsList[i]], res)
            self.backtrack( numsList[:i]+numsList[i+1:] , path+[numsList[i]], res)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return permutations(nums)
        
        res = []
        self.backtrack(nums, [], res)
        return res
        