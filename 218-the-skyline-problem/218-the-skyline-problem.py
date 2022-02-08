from heapq import heappop, heappush, heapify
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for (start, end, height) in buildings:
            points.append((start, height, -1)) # -1 => orientation => indicating its start
            points.append((end, height, 1)) # 1 => orientation => indicating its end
            
        points.sort(key = lambda x: (x[0], x[1]*x[2])) # sorting based on x co-ordinate & if its same then on height of start point
        
        res = []
        activeHeights = [] # use max heap here to increase efficiency
        
        currHeight = 0
        activeHeights.append(currHeight)
        
        for x, height, orientation in points:
            if orientation == -1: # start
                activeHeights.append(height)
            else: # end
                activeHeights.remove(height)
                
            if currHeight != max(activeHeights):
                res.append([x, max(activeHeights)])
                currHeight = max(activeHeights)

        return res