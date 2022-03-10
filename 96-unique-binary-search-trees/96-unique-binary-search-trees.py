class Solution: # Catalan number
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1) # it will store no of BST can be made by i num of nodes
        dp[0] = 1 # one BST can be made with 0 nodes => empty bst
        dp[1] = 1 # one BST can be made with 1 nodes => BST with single node
        
        for i in range(2, n+1):
            left = 0 # nodesOnLeft => if root is a node and on left there are 0 nodes and 
            right = i-1 # nodesOnRight => on right side there are i-1 nodes 
            
            while left <= i-1:
                dp[i] += dp[left] * dp[right] 
                
                left += 1
                right -= 1
                
        return dp[n]

    #     dp[nodesOnLeft] * dp[nodesOnRight]  
    # dp[2] = dp[0]*dp[1] + dp[1]*dp[0]
    # dp[3] = dp[0]*dp[2] + dp[1]*dp[1] + dp[2]*dp[0]
    # dp[4] = dp[0]*dp[3] + dp[1]*dp[2] + dp[2]*dp[1] + dp[3]*dp[0]
    