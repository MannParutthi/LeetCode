class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 : return 0
        
        MAX_NUM = 2 ** 31 - 1
        MIN_NUM = -2 ** 31
        
        sign = 1
        res = 0
        
        index = 0
        if s[0] == "-":
            sign = -1
            index += 1
        elif s[0] == "+":
            sign = 1
            index += 1 
        
        while index < len(s) and s[index].isdigit():
            res = (res*10) + int(s[index])
            index += 1
            
        return max(MIN_NUM, min(sign*res, MAX_NUM))
        
        