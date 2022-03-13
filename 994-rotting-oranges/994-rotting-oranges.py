class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = [] # using BFS
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # count no of fresh oranges
                    freshCount += 1
                if grid[i][j] == 2: # add the location of rotten oranges in queue
                    q.append([i,j])
        
        time = 0           
        adjacentDirections = [[0,1], [0,-1], [1,0], [-1,0]] # left, right, up, down
        while q and freshCount > 0:
            time += 1
            for i in range(len(q)):
                rowNo, colNo = q.pop(0) # row & col no of rotten orange
                for dirRow, dirCol in adjacentDirections: # check left, right, up, down
                    adjRow = dirRow + rowNo 
                    adjCol = dirCol + colNo
                    
                    # if out of bounds or not fresh(1) orange => continue ; else => make it as rotten(2)
                    if adjRow < 0 or adjRow == len(grid) or adjCol < 0 or adjCol == len(grid[0]) or grid[adjRow][adjCol] != 1:
                        continue
                    else:
                        grid[adjRow][adjCol] = 2
                        q.append([adjRow, adjCol])
                        freshCount -= 1            
        
        return time if freshCount == 0 else -1
       