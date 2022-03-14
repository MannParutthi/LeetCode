class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        hashMap = defaultdict(int) # time%60 : freq
        
        for t in time:
            if t % 60 == 0:
                count += hashMap[0]
            else:
                count += hashMap[60 - (t % 60)] # remaining time
            hashMap[t%60] += 1
            
        return count