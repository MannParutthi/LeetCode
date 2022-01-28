class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        res = []
        while left < right and top < bottom:
            for j in range(left, right): # top layer
                res.append(matrix[top][j])
            top +=1
            
            for i in range(top, bottom): # right layer
                res.append(matrix[i][right-1])
            right -= 1
            
            if not(left < right and top < bottom):
                break
                
            for j in range(right-1, left-1, -1): # bottom layer
                res.append(matrix[bottom-1][j])
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1): # left layer
                res.append(matrix[i][left])
            left += 1

        return res
        