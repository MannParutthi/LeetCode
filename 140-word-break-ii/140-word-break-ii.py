class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        if s in wordDict:
            result.append(s)
        
        for i in range(len(s)):
            leftSubStr = s[0:i]
            if leftSubStr in wordDict:
                rightSubStrList = self.wordBreak(s[i:], wordDict)
                for rightSubStr in rightSubStrList:
                    result.append(leftSubStr + " " + rightSubStr)
                    
        return result