class Solution:
    
    def callBFS(self, grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]) or grid[i][j]=="0": #checking boundary conditions
            return
        grid[i][j] = "0" # marking land to water so that its not visited again
        self.callBFS(grid, i-1, j) #up
        self.callBFS(grid, i+1, j) #down
        self.callBFS(grid, i, j-1) #left
        self.callBFS(grid, i, j+1) #right
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    count += 1
                    self.callBFS(grid, i, j)
        return count