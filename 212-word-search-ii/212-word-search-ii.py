class Solution:
    def dfs(self,i, j, board, word, node, visited, result):
        if node.isWord:
            result.append(node.word)
            node.isWord = False
                
        if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and (not visited[i][j]) and board[i][j] in node.children:
            visited[i][j] = True 
            self.dfs(i+1, j, board, word, node.children[board[i][j]], visited, result)
            self.dfs(i-1, j, board, word, node.children[board[i][j]], visited, result)
            self.dfs(i, j+1, board, word, node.children[board[i][j]], visited, result)
            self.dfs(i, j-1, board, word, node.children[board[i][j]], visited, result)
            visited[i][j] = False
            
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trieRoot = TrieNode()
        for word in words:
            trieRoot.addWord(word)
            
        result = []
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board, "", trieRoot, visited, result)

        return result
        
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word =""
    
    def addWord(self, word):
        for char in word:
            if char not in self.children:
                self.children[char] = TrieNode()
            self = self.children[char]
        self.isWord = True
        self.word = word
        