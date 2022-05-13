class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x : x[1])
        
        dp = [1] * len(pairs) # it will store longest chain formed considering itself as the last pair 
        
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]: # b < c
                    dp[i] = max(dp[i], dp[j]+1)
                    
        return max(dp)
    