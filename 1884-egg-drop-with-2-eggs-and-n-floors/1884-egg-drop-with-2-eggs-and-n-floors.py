class Solution:
    def twoEggDrop(self, n: int) -> int:
        noOfEggs = 2
        noOfFloors = n
        dp = [[0]*(noOfFloors+1) for x in range(noOfEggs+1)]
        
        # when floor=0 => no of attempts/moves=0 & floor=1 => no of attempts/moves=1
        for e in range(1, noOfEggs+1):
            dp[e][0] = 0
            dp[e][1] = 1
            
        # when only 1 egg is there =>  no of attempts/moves = no of floors
        for f in range(1, noOfFloors+1):
            dp[1][f] = f
        
        # min of all max / best of all worst
        for e in range(2, noOfEggs+1):
            for f in range(2, noOfFloors+1):
                dp[e][f] = float('inf')
                for x in range(1, f+1): # on x floor => it breaks or survives
                    res = 1 + max(dp[e-1][x-1] , dp[e][f-x]) # breaks , survives
                    dp[e][f] = min(dp[e][f], res)
                    
        return dp[noOfEggs][noOfFloors]