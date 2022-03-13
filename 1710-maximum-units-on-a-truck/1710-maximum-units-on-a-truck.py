class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: (x[1]), reverse=True)
        
        maxUnits = 0
        index = 0
        while truckSize > 0 and index < len(boxTypes):
            noOfBoxes = boxTypes[index][0]
            unitsPerBox = boxTypes[index][1]
            
            if noOfBoxes <= truckSize: # take all boxes
                maxUnits += (noOfBoxes * unitsPerBox)
                truckSize -= noOfBoxes
            else:
                noOfBoxesCanTake = truckSize
                maxUnits += (noOfBoxesCanTake * unitsPerBox)
                truckSize -= noOfBoxesCanTake
                
            index += 1
        
        return maxUnits
        
        