class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSet = set()
        boxSet = set()
        for rowIndex in range(9):
            for colIndex in range(9):
                currVal = board[rowIndex][colIndex]
                if currVal != ".":
                    if (currVal, rowIndex) in rowSet or (currVal, colIndex) in colSet or (currVal, rowIndex//3, colIndex//3) in boxSet :
                        return False
                
                    rowSet.add((currVal, rowIndex))
                    colSet.add((currVal, colIndex))
                    boxSet.add((currVal, rowIndex//3, colIndex//3))
        return True
