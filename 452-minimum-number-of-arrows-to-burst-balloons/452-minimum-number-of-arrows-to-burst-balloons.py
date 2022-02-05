class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        points.sort(key = lambda x: x[1]) # sorting based on balloon end position i.e index 1
        arrowPos = points[0][1] # fire arrow on the end position of first balloon (sorted array => baloon ending first)
        arrowCount = 1
        
        for i in range(1, len(points)):
            if arrowPos >= points[i][0]: # check if arrow fired was at the position after the curr balloon's start point
                continue
            else: # else fire a new arrow at the end position of curr balloon
                arrowCount += 1
                arrowPos = points[i][1]
        return arrowCount