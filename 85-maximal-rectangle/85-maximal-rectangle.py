class Solution: # Using 84 Largest Rectangle in Histogram- https://leetcode.com/problems/largest-rectangle-in-histogram/
    def prevSmallerElesIndex(self, arr):
        res = []
        stack = []
        for i in range(len(arr)):
            while len(stack) > 0 and not arr[stack[-1]] < arr[i]: # if ele in stack is not smaller then curr ele of arr 
                stack.pop()
            if len(stack) == 0:
                res.append(-1) # no prev ele is smaller than curr ele => all are bigger values
            else:
                res.append(stack[-1])
            stack.append(i)
        return res
            
    def nextSmallerElesIndex(self, arr):
        res = []
        stack = []
        for i in range(len(arr)-1, -1, -1):
            while len(stack) > 0 and not arr[stack[-1]] < arr[i]: # if ele in stack is not smaller then curr ele of arr 
                stack.pop()
            if len(stack) == 0:
                res.append(len(arr)) # no next ele is smaller than curr ele => all are bigger values
            else:
                res.append(stack[-1])
            stack.append(i)
        return res[::-1] # reverse of result as we used reverse for loop
    
    
    def maxHistogram(self, heights: List[int]) -> int: # 
        prevSmallerEleIndexArr = self.prevSmallerElesIndex(heights)
        nextSmallerEleIndexArr = self.nextSmallerElesIndex(heights)
        
        maxArea = 0 # (no of bigger values on left + 1 + no of bigger values on right) * height of current ele
        for i in range(len(heights)):
            currArea = (nextSmallerEleIndexArr[i] - prevSmallerEleIndexArr[i] - 1) * int(heights[i])
            maxArea = max(maxArea, currArea)
        return maxArea
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        currRow = [int(x) for x in matrix[0]]
        maxRec = self.maxHistogram(currRow) # find histogram at curr row
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 1:
                    currRow[j] += 1
                else:
                    currRow[j] = 0
            maxRecUsingCurrRow = self.maxHistogram(currRow)
            maxRec = max(maxRec, maxRecUsingCurrRow)
        return maxRec