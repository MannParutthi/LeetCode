class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        digitLogs = []
        for log in logs:
            if (log.split()[1]).isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log.split())
                
        letterLogs.sort(key = lambda x: x[0]) # sorted by identifiers
        letterLogs.sort(key = lambda x: x[1:]) # sorted lexicographically by their contents
        for i in range(len(letterLogs)):
            letterLogs[i] = " ".join(letterLogs[i])
        
        return letterLogs + digitLogs