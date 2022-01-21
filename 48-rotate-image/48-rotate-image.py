class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
#         Converting rows into cols => 1st row will be 1st col , nth row will be nth col (transpose of a matrix)
        for i in range(0,n):
            for j in range(i+1,n):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
        
#         swap cols 0 to last and 1 to last-1 (flip horizontally)
        for i in range(0,n):
            for j in range(0,n//2):
                matrix[i][j] , matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
            
        
        