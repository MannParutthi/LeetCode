class Solution:
    @lru_cache(maxsize=None)
    def dfs(self, string):
        if len(string) > 0 and string[0] == '0': # "06" not valid
            return 0
        if string == "" or len(string) == 1: # traversed whole string
            return 1
        
        if int(string[0:2]) <= 26: # A to Z => 1 to 26 range
            first = self.dfs(string[1:]) # take one digit and pass on
            second = self.dfs(string[2:]) # take 2 digits and pass on
            return first+second
        else:
            return self.dfs(string[1:]) # take only 1st char as the first 2 digits are > 26
    
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0
        return self.dfs(s)