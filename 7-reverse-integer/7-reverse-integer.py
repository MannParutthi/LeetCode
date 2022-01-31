class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(abs(x))[::-1])
        if -2**31 <= ans < 2 **31:
            if x < 0:
                return -ans
            else:
                return ans
        else:
            return 0