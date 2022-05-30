class Solution: # from a cell we can go to cell whose height is "less than or equal to" the curr one
    
    def dfs(self, row, col, visited, prevHeight, noOfRows, noOfCols, heights):
        if ( (row, col) in visited or # if already visited
            row < 0 or col < 0 or row >= noOfRows or col >= noOfCols or # out of bounds
            heights[row][col] < prevHeight # we are going from ocean to cell (inside to outside) so allowed is >=
        ):
            return
        
        visited.add((row, col)) # we can visit from ocean to cell => so from this cell we can go to ocean
        self.dfs(row + 1, col, visited, heights[row][col], noOfRows, noOfCols, heights) # south
        self.dfs(row - 1, col, visited, heights[row][col], noOfRows, noOfCols, heights) # north
        self.dfs(row, col + 1, visited, heights[row][col], noOfRows, noOfCols, heights) # east
        self.dfs(row, col - 1, visited, heights[row][col], noOfRows, noOfCols, heights) # west
            
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        noOfRows = len(heights)
        noOfCols = len(heights[0])
        
        pacific = set() # will store cells from which pacific ocean can be visited
        atlantic = set() # will store cells from which atlantic ocean can be visited
        
        for col in range(noOfCols): # 1st row => pacific border , last row => atlantic border
            self.dfs(0, col, pacific, heights[0][col], noOfRows, noOfCols, heights)
            self.dfs(noOfRows-1, col, atlantic, heights[noOfRows-1][col], noOfRows, noOfCols, heights)
            
        for row in range(noOfRows): # 1st col => pacific border , last col => atlantic border
            self.dfs(row, 0, pacific, heights[row][0], noOfRows, noOfCols, heights)
            self.dfs(row, noOfCols-1, atlantic, heights[row][noOfCols-1], noOfRows, noOfCols, heights)
            
        res = [] # if from a cell both pacific & atlantic can be visited => add to result
        for row in range(noOfRows):
            for col in range(noOfCols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
                    
        return res