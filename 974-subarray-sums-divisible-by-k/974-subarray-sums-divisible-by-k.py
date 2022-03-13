class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashMap = {} # remainder : frequency
        result = 0
        total = 0
        remainder = 0
        
        hashMap[0] = 1
        for number in nums:
            total += number
            remainder = total % k
            
            if remainder < 0:
                remainder += k
                
            if remainder in hashMap:
                result += hashMap[remainder]
                hashMap[remainder] += 1
            else:
                hashMap[remainder] = 1
                
        return result