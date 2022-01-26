class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1) # here dp[i] stores min coins req to make amount i
        dp[0] = 0
        
        for amt in range(1, len(dp)): # 1 to amount - both inclusive
            for coinVal in coins:
                if coinVal <= amt:
                    dp[amt] = min(dp[amt-coinVal]+1 , dp[amt])
                    
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
        