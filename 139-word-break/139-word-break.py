class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1) # one extra element for base case
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1): # reverse for loop from last element
            for word in wordDict:
                if i+len(word) <= len(s) and s[i: i+len(word)] == word:
                    dp[i] = dp[i+len(word)] 
                    # True only if there is a word starting at index => i+len(word) => i.e new word starts where this one ends
                if dp[i] == True:
                    break
                    
        return dp[0] # dp stores if a word is starting at index i and it has others words following it 