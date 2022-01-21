class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x: x[0])
        
        res = [intervals[0]]
        for index in range(1, len(intervals)):
            if res[-1][1] >= intervals[index][0]:
                res[-1][1] = max(res[-1][1], intervals[index][1])
            else:
                res.append(intervals[index])
                
        return res
            
