class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        neighbours = collections.defaultdict(list) # adjacency list => graph => with word of similar patterns e.g. AB*, A*C, *BC 
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbours[pattern].append(word)
        
        visited = [beginWord]
        queue = [beginWord]
        res = 1
        while queue: # BFS
            for i in range(len(queue)):
                word = queue.pop(0)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in visited:
                            visited.append(neighbour)
                            queue.append(neighbour)
                            
            res += 1 # no of layers / levels to reach the endWord
        return 0