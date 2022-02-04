class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndex = {} # it stores last index of all chars  
        
        for index, ch in enumerate(s):
            lastIndex[ch] = index 
            
        resultStack = []
        for i, ch in enumerate(s):
            if ch not in resultStack: # check if curr char < last char in stack & that last char are left in string => remove it 
                while len(resultStack) > 0 and ch < resultStack[-1] and i < lastIndex[resultStack[-1]]:
                    resultStack.pop()
                resultStack.append(ch)
        
        return ''.join(resultStack)