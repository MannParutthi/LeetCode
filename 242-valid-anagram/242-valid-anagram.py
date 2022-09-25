class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterDict = {}
        for ele in s:
            if ele not in counterDict:
                counterDict[ele] = 1
            else:
                counterDict[ele] += 1
        for ele in t:
            if ele not in counterDict:
                return False
            else:
                counterDict[ele] -= 1
        for val in counterDict.values():
            if val != 0:
                return False
        return True
                
        # return sorted(s) == sorted(t)