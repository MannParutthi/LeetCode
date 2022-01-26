class Solution:
    def trailingZeroes(self, n: int) -> int:
        # every alternate / second number is a multiple of 2 => 2, 4, 6, 8, 10, ...
        # every fith number is a multiple of 5 => 5, 10, 15, 20, ...
        # trailing 0 is nothing but multiple of 10 => if we find no of 10's we can find trailing zeros
        # 10 is formed by 2 * 5 => i.e. 2^x * 5^y - in this min(x,y) will be no of 10's
        # as we know that from 1 to N, 2 comes more times (alternate no) as compared to 5 (fifth no)
        # if we just find power of 5 - it will be the answer => 5^x - x is the answer
        # Formula => floor(n/5) + floor(n/25) + floor(n/125) + floor(n/5^4) + ...... + floor(n/5^x)
        
        noOfTrailingZeros = 0
        divisor = 5
        
        while divisor <= n:
            noOfTrailingZeros += n//divisor
            divisor *= 5
            
        return noOfTrailingZeros