class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currDir = "N"
        x = 0
        y = 0
        
        for instruction in instructions:
            if instruction == "G":
                if currDir == "N": y += 1 
                if currDir == "S": y -= 1
                if currDir == "E": x += 1
                if currDir == "W": x -= 1 
            else: # L or R
                if currDir == "N":
                    if instruction == "L": currDir = "W" 
                    else: currDir = "E"
                
                elif currDir == "W":
                    if instruction == "L": currDir = "S"  
                    else: currDir = "N"
                
                elif currDir == "S":
                    if instruction == "L": currDir = "E"
                    else: currDir = "W"
                    
                elif currDir == "E":
                    if instruction == "L": currDir = "N" 
                    else: currDir = "S"

        if (x == 0 and y == 0) or currDir != "N":
            return True
        else:
            return False