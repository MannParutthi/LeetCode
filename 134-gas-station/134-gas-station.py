class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        gasInTank = 0
        resIndex = 0
        for i in range(len(gas)):
            gasInTank += (gas[i] - cost[i])
            
            if gasInTank < 0:
                resIndex = i+1
                gasInTank = 0
                
        return resIndex