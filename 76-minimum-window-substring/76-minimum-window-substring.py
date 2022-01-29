from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0 # Left Index Ptr
        right = 0 # Right Index Ptr
        
        matchCount = 0
        minWindowLen = float('inf')
        minWindowStr = ""
        
        freqOfTargetStr = Counter(t)
        freqOfMatchSearchStr = defaultdict(int) # int => default value 0 & defaultdict => doesnt give KeyError if ele not found
        
        # increment right ptr till match is found and after then increment left ptr till match is lost (remove char's and try to               shorten the window), once match is lost again start incrementing the right ptr  
        while right < len(s):
            freqOfMatchSearchStr[s[right]] += 1
            if s[right] in freqOfTargetStr:
                if freqOfMatchSearchStr[s[right]] <= freqOfTargetStr[s[right]]:
                    matchCount += 1
            
            while left <= right and matchCount == len(t): # while current window contains perfect match
                currWindowLen = right - left + 1
                if currWindowLen < minWindowLen: # checking if current window length is less then replacing it with the result
                    minWindowLen = currWindowLen
                    minWindowStr = s[left : right+1]
            
                freqOfMatchSearchStr[s[left]] -= 1 # incrementing left ptr and removing left char from match
                if s[left] in freqOfTargetStr and freqOfMatchSearchStr[s[left]] < freqOfTargetStr[s[left]]:
                    matchCount -= 1
                left += 1
                
            right += 1 # incrementing right ptr once match is lost / there is no more perfect match
        
        return minWindowStr