class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele in ['+', '-', '*', '/']:
                y = int(stack.pop())
                x = int(stack.pop())
                if ele == '+':
                    stack.append(x + y)
                elif ele == '-':
                    stack.append(x - y)
                elif ele =='*':
                    stack.append(x * y)
                elif ele == '/':
                    stack.append(int(x / y))
            else: 
                stack.append(ele)
                
        return stack[-1]
        