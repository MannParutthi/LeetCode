class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # newInterval('s end) is before intervals[i]
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # newInterval('s start) is after intervals[i]
                res.append(intervals[i])
            else: # overlapping
                newInterval = [ min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]) ]
        
        res.append(newInterval) # if overlapping with the last one then we need to add otherwise the if cond handles it
        return res