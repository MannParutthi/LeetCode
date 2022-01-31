class Solution:
    def helper(self, x, n): # Odd => x * x^2 * x^2 = x^5 & Even => x^2 * x^2 = x^4
            if n == 0: return 1
            
            res = self.helper(x, n//2)
            res = res*res
            
            if n%2 == 0: # Even
                return res 
            else: # Odd
                return res*x 
    
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        
        res = self.helper(x, abs(n))
        
        if n>=0:
            return res
        else: # x^-2 == 1/x^2 => x^-n == 1/x^n
            return 1/res