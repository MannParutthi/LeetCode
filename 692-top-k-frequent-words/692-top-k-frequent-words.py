class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordFreq = defaultdict(int) # word : freq
        for word in words:
            wordFreq[word] += 1
        
        wordFreq = sorted(wordFreq.items(), key = lambda x:(-x[1], x[0]))
        
        res = []
        for i in range(k):
            res.append(wordFreq[i][0])
            
        return res
        