class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(nums) != len(set(nums))
        dictAlreadyVisited = {}
        for ele in nums:
            if ele in dictAlreadyVisited:
                return True
            else:
                dictAlreadyVisited[ele] = 1