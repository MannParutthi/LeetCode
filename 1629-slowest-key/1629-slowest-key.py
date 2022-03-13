class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        pressDuration = {} # key : time duration
        for i in range(len(releaseTimes)):
            key = keysPressed[i]
            if i == 0:
                pressDuration[key] = releaseTimes[i]
            else:
                pressDuration[key] = max(pressDuration.get(key, 0), releaseTimes[i] - releaseTimes[i-1])
                
        sortedDict = sorted(pressDuration.items(), key = lambda x:(x[1], x[0]), reverse = True)
        return sortedDict[0][0]