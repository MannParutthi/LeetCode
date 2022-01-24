class Solution:
    
    def wordBreakHelper(self, s, wordDict, hashMap):
        if s in hashMap:
            return hashMap[s]
            
        result = []
        if s in wordDict:
            result.append(s)
        
        for i in range(len(s)):
            leftSubStr = s[0:i]
            if leftSubStr in wordDict:
                rightSubStrList = self.wordBreakHelper(s[i:], wordDict, hashMap)
                for rightSubStr in rightSubStrList:
                    result.append(leftSubStr + " " + rightSubStr)
        
        hashMap[s] = result    
        return result
    
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.wordBreakHelper(s, wordDict, {})