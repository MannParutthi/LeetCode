class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int) # stores sum and its freq
        hashMap[0] = 1
        
        summ = 0
        res = 0
        for i in range(len(nums)):
            summ += nums[i]
            if (summ - k) in hashMap:#if (sum-target) in hashmap then sum till i & subtract (sum-target) freq times
                res += hashMap[summ-k]
            hashMap[summ] += 1
        return res