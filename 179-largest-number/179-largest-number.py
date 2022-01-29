import functools
class Solution:
    def comparator(self, x, y):
        if x+y > y+x: # x > y
            return 1
        elif x+y < y+x: # x < y
            return -1
        else:
            return 0
    
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        nums.sort(key = functools.cmp_to_key(self.comparator) , reverse=True)
        
        if nums and nums[0] == '0':
            return '0'
        
        return ''.join(nums)