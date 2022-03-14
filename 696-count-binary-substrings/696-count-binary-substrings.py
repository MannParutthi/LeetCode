class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevGroupCount = 0 # making groups of 0's and 1's e.g. = 0011 => prevGroupCount = 2 & currGroupCount = 2
        currGroupCount = 1 
        
        res = 0
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res += min(prevGroupCount, currGroupCount) # it should have same no of 0's and 1's so we are taking min
                prevGroupCount = currGroupCount
                currGroupCount = 1
            else:
                currGroupCount += 1

        res += min(prevGroupCount, currGroupCount)
        
        return res