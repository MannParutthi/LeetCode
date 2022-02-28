class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)] # empty string to full string

        for i in range(len(dp)): # i pointer for pattern
            for j in range(len(dp[0])): # j pointer for string
                if i == 0 and j == 0: # 1st col 1st row dp[0][0] # empty / null => S & P
                    dp[i][j] = True
                elif i == 0: # 1st row apart from [0][0] all false => empty pattern cant match with any str
                    dp[i][j] = False
                elif j == 0: # 1st col apart from [0][0]
                    patternChar = p[i-1]
                    if patternChar == "*": # chk 2 rows back => if its S* means it can be 0 or more S
                        dp[i][j] = dp[i-2][j] # so check after considering it as 0 => prevStr + S* => prevStr
                    else: # any pattern char cant match with empty str
                        dp[i][j] = False   
                else:
                    patternChar = p[i-1]
                    stringChar = s[j-1]
                    if patternChar == "*": # if mis* => compare with mi and miss*
                        dp[i][j] = dp[i-2][j] # compare with mi
                        
                        patternSecondLastChar = p[i-2] # compare with miss*
                        if patternSecondLastChar == "." or patternSecondLastChar == stringChar:
                            dp[i][j] = dp[i][j] or dp[i][j-1]
                
                    elif patternChar == ".": # . can cover any char so go to diagonal => s = mis & p = mi. 
                        dp[i][j] = dp[i-1][j-1] # chk for mi == mi or not
                    elif patternChar == stringChar: # compare prev str ignore last char or both => s=mis & p=mis 
                         dp[i][j] = dp[i-1][j-1] # chk for mi == mi or not
                    else:
                        dp[i][j] = False 
                        
        return dp[-1][-1]