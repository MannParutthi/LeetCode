class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictUniqueStr = {}
        for s in strs:
            sortedStr = "".join([str(x) for x in sorted(s)])
            if len(dictUniqueStr) > 0 and sortedStr in dictUniqueStr:
                dictUniqueStr[sortedStr].append(s)
            else:
                dictUniqueStr[sortedStr] = [s]
        return [val for val in dictUniqueStr.values()]