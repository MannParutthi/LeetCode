class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0 or denominator == 0:
            return "0"
        
        if numerator < 0 and denominator < 0:
            isAnsNeg = False
        elif numerator < 0 or denominator < 0:
            isAnsNeg = True
        else:
            isAnsNeg = False
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        ans = ""
        prevRem = {} # it will store prev rem and length of ans at that time so we can insert '(' at that pos 
        
        quo = numerator // denominator
        rem = numerator % denominator
        ans += str(quo)
        
        if rem == 0:
            pass
        else:
            ans += "."
            while rem != 0:
                if rem in prevRem: # repeating part found
                    startIndexOfRepeat = prevRem[rem]
                    ans = ans[:startIndexOfRepeat] + "(" + ans[startIndexOfRepeat:]
                    ans += ")"
                    break
                else:
                    prevRem[rem] = len(ans)
                    rem *= 10
                    quo = rem // denominator
                    rem = rem % denominator
                    ans += str(quo)
                    
        if isAnsNeg: return "-" + ans
        else: return ans