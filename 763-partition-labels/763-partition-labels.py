class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastIndexOfCharMap = {char:index for index, char in enumerate(s)}
        
        currPartitionSize = 0
        lastIndexOfCurrPartition = 0
        for index, char in enumerate(s):
            currPartitionSize += 1
            lastIndexOfCurrPartition = max(lastIndexOfCurrPartition, lastIndexOfCharMap[char])
            
            if index == lastIndexOfCurrPartition:
                res.append(currPartitionSize)
                currPartitionSize = 0
        
        return res