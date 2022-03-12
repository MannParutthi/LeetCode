class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr # we can use += but then we'll need to rev it
                stack.pop() # to pop "["    
                
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                
                stack.append(int(digit) * subStr)
        
        return "".join(stack)