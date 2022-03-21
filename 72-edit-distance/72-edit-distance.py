class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [ [0] * (len(word2)+1) for x in range(len(word1)+1) ] # will store min operations to convert string
        
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                
                if i == 0: # if first string is empty, only option is to insert all characters of second string
                    dp[i][j] = j
                    
                elif j == 0: # if second string is empty, only option is to remove all characters of second string
                    dp[i][j] = i
                    
                elif word1[i-1] == word2[j-1]: #if last chars are same, ignore last char & recur for remaining str
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) # Insert, Remove, Replace
        
        return dp[-1][-1]
    