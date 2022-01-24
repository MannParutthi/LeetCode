class Solution:
    def calculate(self, s: str) -> int:
        s+="+0" # for loop ends so last operation cant be done so by adding this +0 it can be completed
        stack = []
        num = 0
        opr = "+" # by default first char is digit and its positive
        
        for i in range(len(s)):
            if s[i].isdigit(): 
                num = num*10 + int(s[i]) # for 2 or more digit number
            elif s[i] in ["+", "-", "*", "/"] or i == len(s)-1: # using prev sign / opr => e.g +2 -3 *4 /5
                if opr == "+":   stack.append(num)
                elif opr == "-": stack.append(-num)
                elif opr == "*": stack.append(stack.pop() * num)
                elif opr == "/": stack.append(int(stack.pop() / num))
                num = 0
                opr = s[i] # assigning sign / opr for next time use
                # this num & opr are not used for last index so we have added +0 at the end of the string in the start
            elif s[i].isspace():
                continue
        print(stack, num, opr)        
        return sum(stack)
        