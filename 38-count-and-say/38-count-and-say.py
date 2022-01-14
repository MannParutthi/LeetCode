class Solution:
    
    def getCountAndSayStr(self, n):
        if n == 1: return "1"
        
        sayStr = ""
        lastUniqueEle = str(n)[0]
        countOfLastUniqueEle = 0
        
        for ele in str(n):
            if ele == lastUniqueEle:
                countOfLastUniqueEle += 1
            else:
                sayStr += str(countOfLastUniqueEle) + str(lastUniqueEle)
                lastUniqueEle = ele
                countOfLastUniqueEle = 1
        sayStr += str(countOfLastUniqueEle) + str(lastUniqueEle)
        
        return sayStr
    
    def countAndSay(self, n: int) -> str:
        val = 1
        count = 0
        while count < n:
            val = self.getCountAndSayStr(val)
            count+=1
        return val

            