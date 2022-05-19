class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0]*len(matrix[0]) for x in range(len(matrix))] 
        # each cell will store max square that can be made considering itself as the top left corner
        res = float('-inf') # longest square side
        
        # start from bottom right corner cell
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                if i == len(dp)-1 or j == len(dp[0])-1: # bottom (last) row or right-most (last) col
                    dp[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 0:
                        dp[i][j] = 0
                    else:
                        minSq = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1]) # check bottom, right & diagonal   
                        dp[i][j] = minSq + 1
                res = max(res, dp[i][j])

        return res**2 # area = side * side                    