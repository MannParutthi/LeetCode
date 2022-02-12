class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            prefix = s[:i]
            remainingString = s[i:]
            if self.isPalindrome(prefix):
                self.dfs(remainingString, path+[prefix], res)
    
    def isPalindrome(self, s):
        return s == s[::-1]    
        