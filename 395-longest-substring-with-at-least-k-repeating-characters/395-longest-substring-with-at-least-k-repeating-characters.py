class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        
        freqDict = {}
        for char in s:
            if char in freqDict: freqDict[char] += 1
            else: freqDict[char] = 1
        
        longestSubStrLen = 0
        startIndex = 0
        valid = True
        for endIndex, char in enumerate(s):
            if freqDict[char] < k:
                longestSubStrLen = max(longestSubStrLen, self.longestSubstring(s[startIndex : endIndex], k))
                startIndex = endIndex+1
                valid = False
        
        if valid: return len(s)
        else: return max(longestSubStrLen, self.longestSubstring(s[startIndex:], k))
        