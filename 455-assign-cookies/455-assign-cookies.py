class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        childsGreedPtr = 0 # index of child => prev index means child satisfied
        cookieSizePtr = 0 # index of cookie => prev index means used
        
        while childsGreedPtr < len(g) and cookieSizePtr < len(s):
            if g[childsGreedPtr] <= s[cookieSizePtr]:
                childsGreedPtr += 1 # child satisfied
                cookieSizePtr += 1 # as it is used
            else:
                cookieSizePtr += 1
                
        return childsGreedPtr # no of child satisfied