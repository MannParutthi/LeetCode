class Solution:
    def dfs(self,i, j, board, wordIndex, word, visited):
        if wordIndex > len(word) - 1:
            return True
        if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and (not visited[i][j]) and board[i][j] == word[wordIndex]:
            visited[i][j] = True 
            foundNextChar = self.dfs(i+1, j, board, wordIndex+1, word, visited) or \
                            self.dfs(i-1, j, board, wordIndex+1, word, visited) or \
                            self.dfs(i, j+1, board, wordIndex+1, word, visited) or \
                            self.dfs(i, j-1, board, wordIndex+1, word, visited)
            visited[i][j] = False
            return foundNextChar
        else:
            return False
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i, j, board, 0, word, visited):
                    return True
        return False