class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2: 
            return len(points)
        
        d = collections.defaultdict(int) # slope : count
        result = 0
        for i in range(len(points)):
            d.clear()
            overlap, curmax = 0, 0
            for j in range(i+1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    overlap += 1 # points on same axis y=0 or x=0
                    
                if dx != 0:
                    slope = dy * 1.0 / dx
                else:
                    slope = float("inf")
                d[slope] += 1
                
                curmax = max(curmax, d[slope]) # currmax => points with same slope
                
            result = max(result, curmax + overlap + 1) # 1 for itself
        return result