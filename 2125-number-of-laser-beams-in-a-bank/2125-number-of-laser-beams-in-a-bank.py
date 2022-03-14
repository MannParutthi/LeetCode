class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [list(x) for x in bank] 
        connections = 0
        
        prevNodes = bank[0].count('1')
        
        for floor in bank[1:]:
            currNodeCount = floor.count('1')
            if currNodeCount >= 1:
                connections += currNodeCount * prevNodes
                prevNodes = currNodeCount
                
        return connections