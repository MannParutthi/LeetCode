class Solution: # same as 647. Palindromic Substrings
    
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)): # expanding from middle to left and right and checking for palindromes
            # odd length
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > resLen:
                    res = s[left : right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
                
            # even length
            left = i
            right = i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > resLen:
                    res = s[left : right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
        return res
    
#     def longestPalindrome(self, s: str) -> str:
#         dp = [ [False] * len(s) for x in range(len(s)) ]

#         maxLen = startIdx = 0
#         for i in range(len(s) - 1, -1, -1):
#             for j in range(i, len(s)):
#                 if i == j:
#                     dp[i][j] = True
#                 elif s[i] == s[j]:
#                     dp[i][j] = (i+1 == j) or dp[i + 1][j - 1]

#                 if dp[i][j]:
#                     newLen = j - i + 1
#                     if newLen > maxLen:
#                         maxLen = newLen
#                         startIdx = i

#         return s[startIdx:startIdx + maxLen]
    
#     def longestPalindrome(self, s: str) -> str:
#         dp = [ [False] * len(s) for x in range(len(s)) ] 
#         # left to right => end char index & top to bottom => start char index in matrix
#         # only top triangle will be used and bottom triangle of matrix wont be used as cant have start>end
#         # matrix will store if substr from i (start) index to j (end) index is a palindrome or not 
        
#         maxLenSubStr = s[0]
#         maxLen = 1 # traversing from diagonal of matrix (i==j) to top corner / upwards
#         for gap in range(len(s)): # gap in between index i and j => a[i] to a[j] 
#             i = 0
#             j = gap # gap 'n' means substr of len 'n+1'
#             while j < len(s):
#                 if gap == 0: # single char i.e a / b / c
#                     dp[i][j] = True # single char substr are always palindromic
#                 elif gap == 1: # two char / gap 1 => ab / bb / ca
#                     dp[i][j] = (s[i] == s[j]) # if both char are same then only its palindromic / True
#                 else: # gap is more than 2 => substr of len 3 to n
#                     if s[i] == s[j] and dp[i+1][j-1] == True: # if extreme char at index start & end are same 
#                         dp[i][j] = True # then check if inner substring is palindromic or not => dp[i+1][j-1]
                        
#                 if dp[i][j] == True: # palindromic substr found 
#                     if maxLen < gap+1:
#                         maxLen = gap + 1
#                         maxLenSubStr = s[i:j+1]
            
#                 i += 1 # we are going diagonally in matrix
#                 j += 1 # so incrementing i & j both at the same time
                
#         return maxLenSubStr