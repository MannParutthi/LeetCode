class Solution:
    def maxArea(self, height: List[int]) -> int:
        frontPtr = 0
        rearPtr = len(height) - 1
        
        maxVolume = 0
        while frontPtr < rearPtr:
            volume = (rearPtr - frontPtr) * min(height[rearPtr], height[frontPtr]) 
            maxVolume = max(volume, maxVolume)
            
            if height[frontPtr] < height[rearPtr]:
                frontPtr += 1
            else:
                rearPtr -= 1
                
        return maxVolume
                
            