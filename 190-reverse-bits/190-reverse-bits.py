class Solution:
    def reverseBits(self, n: int) -> int:
        # reverseBin = bin(int(str(n)[::-1]))
        # return int(reverseBin)
        
        res = 0
        for i in range(32):
            res = res<<1 # left shift
            res += n & 1 # last bit
            n = n >> 1 # right shift
        return res