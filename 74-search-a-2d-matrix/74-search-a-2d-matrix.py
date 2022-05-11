class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            top = 0
            bottom = len(matrix) - 1
            
            while top <= bottom:
                midRow = (top + bottom) // 2
                if target > matrix[midRow][-1]:
                    top = midRow + 1
                elif target < matrix[midRow][0]:
                    bottom = midRow - 1
                else:
                    break
            
            if top > bottom:
                return False
            
            resRow = (top + bottom) // 2
            left = 0
            right = len(matrix[0]) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if target > matrix[resRow][mid]:
                    left = mid + 1
                elif target < matrix[resRow][mid]:
                    right = mid - 1
                else:
                    return True
            return False
            
                