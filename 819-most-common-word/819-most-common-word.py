class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        onlyCharStr = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        listOfWords = onlyCharStr.split(" ")
        
        freqMap = {}
        for word in listOfWords:
            word = word.lower()
            if word not in banned and len(word)>0:
                if word in freqMap:
                    freqMap[word] += 1
                else:
                    freqMap[word] = 1
        
        maxFreqCount = 0
        maxFreqWord = ""
        for word, freq in freqMap.items():
            if freq > maxFreqCount:
                maxFreqCount = freq
                maxFreqWord = word
                
        return maxFreqWord