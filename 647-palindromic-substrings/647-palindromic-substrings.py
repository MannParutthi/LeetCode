class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [ [False] * len(s) for x in range(len(s)) ] 
        # left to right => end char index & top to bottom => start char index in matrix
        # only top triangle will be used and bottom triangle of matrix will not be used as cant have start>end
        # matrix will store if substr from i (start) index to j (end) index is a palindrome or not 
        
        count = 0 # traversing from diagonal of matrix (i==j) to top corner / upwards
        for gap in range(len(s)): # gap in between index i and j => a[i] to a[j] 
            i = 0
            j = gap # gap 'n' means substr of len 'n+1'
            while j < len(s):
                if gap == 0: # single char i.e a / b / c
                    dp[i][j] = True # single char substr are always palindromic
                elif gap == 1: # two char / gap 1 => ab / bb / ca
                    dp[i][j] = (s[i] == s[j]) # if both char are same then only its palindromic / True
                else: # gap is more than 2 => substr of len 3 to n
                    if s[i] == s[j] and dp[i+1][j-1] == True: # if extreme char at index start & end are same 
                        dp[i][j] = True # then check if inner substring is palindromic or not => dp[i+1][j-1]
                        
                if dp[i][j] == True: # palindromic substr found 
                    count += 1
            
                i += 1 # we are going diagonally in matrix
                j += 1 # so incrementing i & j both at the same time
                
        return count