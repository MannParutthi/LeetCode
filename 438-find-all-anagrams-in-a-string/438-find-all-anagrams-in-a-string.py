class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        freqOfP = defaultdict(int)
        for char in p:
                freqOfP[char] += 1
        
        currWindowFreqOfS = defaultdict(int)
        for i in range(len(p)):
                currWindowFreqOfS[s[i]] += 1
        
        res = []
        leftPtr = 0
        rightPtr = len(p)-1
        
        while rightPtr < len(s):
            if currWindowFreqOfS == freqOfP:
                res.append(leftPtr)
            
            currWindowFreqOfS[s[leftPtr]] -= 1
            if currWindowFreqOfS[s[leftPtr]] == 0:
                del currWindowFreqOfS[s[leftPtr]]
            leftPtr += 1
            
            rightPtr += 1
            if rightPtr < len(s): currWindowFreqOfS[s[rightPtr]] += 1

        return res 