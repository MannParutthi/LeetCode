class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # below holds true only if dividing by any factor of pow(2) i.e => 1(2^0), 2(2^1), 4(2^2), 8(2^3), 16(2^4)
        # in bitwise operations, if we want to know quotient and remainder without dividing numbers
        # then => 15 / 4 => binary of 15 - 1111 (len 4) & binary of - 100 (len 3)
        # just split the no 15 into two parts 
        # last part should have "len(divisor)-1" digits i.e 2 & remaining should be in 1st part
        # 1111 (15) => first part - 11 (quotient) & last part 11 (quotient)
        # bin 11 is 3 number => quotient = 3 & quotient = 3
        
        # Ex2 => 15 / 2 => 1111 / 10 => split from last (2-1) digits => quotient = 111 (7) & remainder = 1 (1)
        
        # left shift => n << x => n * 2^x
        # right shift => n >> x => n // 2^x
        
        isNegative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0 # we are subtracting divisor from dividend and doubling divisor and trying to subtract it 
        while dividend >= divisor:
            currDivisor = divisor
            count = 1
            while dividend >= currDivisor:
                dividend -= currDivisor
                quotient += count
                
                currDivisor = currDivisor << 1 #(divisor << 1) => doubling divisor => n<<x means n*2^x
                count = count << 1
        
        quotient = -quotient if isNegative else quotient
        return min(max(-2**31, quotient), 2**31-1)
    
    # if 10/3 => checking how many times 3 can be subtracted then how many times (3*2 = double) 6 can be subtracted ... 