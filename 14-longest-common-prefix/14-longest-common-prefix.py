class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        
        for i in range(1, len(strs)):
            size = min(len(strs[i]), len(res))
            for j in range(size, -1, -1):
                if strs[i][:j] == res[:j]:
                    res = res[:j]
                    break
        return res
        