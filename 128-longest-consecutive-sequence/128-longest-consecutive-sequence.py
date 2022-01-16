class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        isNoStartOfSeq = {x:True for x in nums}
        
        for ele in nums:
            if ele-1 in isNoStartOfSeq:
                isNoStartOfSeq[ele] = False # if prev ele exists then setting current value as not start of sequence
        
        maxLenOfSeq = 0
        for no, isSeqStartingFromNo in isNoStartOfSeq.items():
            if isSeqStartingFromNo: # if start of sequence then count no of consecutive elements starting from that ele
                n = no
                countLen = 0
                while n in isNoStartOfSeq:
                    countLen += 1
                    n += 1
                maxLenOfSeq = max(maxLenOfSeq, countLen) 
                
        return maxLenOfSeq