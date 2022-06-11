class Solution: # sliding window problem
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
        
#         freqMap = {} # stores character : freq of the current window
#         res = 0
        
#         leftPtr = 0
#         for rightPtr in range(len(s)):
#             charAtRightPtr = s[rightPtr] # keep adding char as window expands
#             freqMap[charAtRightPtr] = 1 + freqMap.get(charAtRightPtr, 0)
            
#             sizeOfCurrWindow = rightPtr - leftPtr + 1
            
#             # incrementing left ptr when curr window can't be converted to result => while invalid => increment leftPtr
#             while sizeOfCurrWindow - max(freqMap.values()) > k: #only k ele can be replaced : k < freq of max occuring char
#                 charAtLeftPtr = s[leftPtr]
#                 freqMap[charAtLeftPtr] -= 1 
#                 leftPtr += 1

#             res = max(res, sizeOfCurrWindow) # sizeOfCurrWindow is valid result which can be formed by replacing at most k char
            
#         return res
