class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[0],x[1]))
        
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if  start >= prevEnd: # not overlapping
                prevEnd = end
            else: # overlapping
                res += 1
                prevEnd = min(prevEnd, end) # delete which is longer => greater end val
        return res