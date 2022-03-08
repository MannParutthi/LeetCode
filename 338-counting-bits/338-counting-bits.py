class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1) # it stores no of 1's in all values from 0 to n+1
        
        for i in range(1, n+1):
            if i%2 == 0: # even
                res[i] = res[i//2]
            else: # odd
                res[i] = res[i//2] + 1
            
        return res
    
    # no of 1's in 0 = 0
    # no of 1's in 1 = res[0] + 1
    # no of 1's in 2 = res[1]
    # no of 1's in 3 = res[1] + 1
    # no of 1's in 4 = res[2]
    # no of 1's in 5 = res[2] + 1