class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # sliding window
        res = 0 # valid substr len
        rightPtr = -1
        leftPtr = -1
        charFreqMap = {}
        
        while True:
            isAcquired = False
            isReleased = False
            
            # acquire - acquire until it becomes invalid
            while rightPtr < len(s)-1:
                isAcquired = True
                rightPtr += 1
                if s[rightPtr] not in charFreqMap: charFreqMap[s[rightPtr]] = 1
                else: charFreqMap[s[rightPtr]] += 1
                
                if charFreqMap[s[rightPtr]] == 2: # it became invalid
                    break
                else:    
                    if rightPtr-leftPtr > res: # if valid store it in result if its better than prev result
                        res = rightPtr - leftPtr # rightPtr - leftPtr => len of valid substr
            
            # release - release until it becomes valid
            while leftPtr < rightPtr:
                isReleased = True
                leftPtr += 1
                charFreqMap[s[leftPtr]] -= 1
                
                if charFreqMap[s[leftPtr]] == 1: # it became valid
                    break
            
            if not isAcquired and not isReleased:
                break
                
        return res
                    