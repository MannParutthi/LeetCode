class Solution: # https://youtu.be/NbgUZAoIz3g
    
    def isMatch(self, s: str, p: str) -> bool: # traverse from right bottom corner
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)] # from all chars to empty
        
        for i in range(len(dp)-1, -1, -1): # i pointer for pattern => reverse for loop from ij to 00
            for j in range(len(dp[0])-1, -1, -1): # j pointer for string  => bottom right to top left
                if i == len(dp)-1 and j == len(dp[0])-1: # last cell => right bottom corner
                    dp[i][j] = True # blank pattern matches blank string
                elif i == len(dp)-1: # last row => blank pattern cant match any string (non-empty)
                    dp[i][j] = False
                elif j == len(dp[0])-1: # last col
                    if p[i] == "*": # check below value
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = False
                else:
                    if p[i] == "?" or p[i] == s[j]: # chk diagonal
                        dp[i][j] = dp[i+1][j+1]
                    elif p[i] == "*": # check below value (vertical) or next val (horizontal) 
                        dp[i][j] = dp[i+1][j] or dp[i][j+1]
                    else:
                        dp[i][j] = False
                        
        return dp[0][0]
                    