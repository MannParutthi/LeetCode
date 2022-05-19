class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        charStack = [] # can be removed to save space
        indexStack = [] # it will store the indexes of location where parentheses is invalid 
        indexStack.append(-1) # wil be helpful for calculating length
        
        for i in range(len(s)):
            if s[i] == '(':
                charStack.append('(')
                indexStack.append(i)
            elif s[i] == ')':
                if len(charStack) > 0 and charStack[-1] == '(': # valid combination found so pop
                    charStack.pop()
                    indexStack.pop()
                    maxLen = max(maxLen, i - indexStack[-1]) # indexStack[-1] => will have index till where its invalid
                else:
                    indexStack.append(i) # at i - parentheses is invalid 
                    
        return maxLen
        