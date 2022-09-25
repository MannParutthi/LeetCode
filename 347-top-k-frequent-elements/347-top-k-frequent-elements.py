class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for ele in nums:
            if ele in freqDict:
                freqDict[ele] += 1
            else:
                freqDict[ele] = 1
        freqOrderedDict = sorted(freqDict.items(), key=lambda item: item[1], reverse=True)
        res = []
        for i in range(k):
            res.append(freqOrderedDict[i][0])
        return res
                
        
        