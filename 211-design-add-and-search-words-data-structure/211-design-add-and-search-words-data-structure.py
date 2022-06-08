class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True            

    def dfs(self, startIndex, root, word): # helper func for search
        curr = root
        for i in range(startIndex, len(word)):
            char = word[i]
            if char == ".": # wild card char
                for child in curr.children.values(): # all childs => .values() for getting all val from hashmap 
                    if self.dfs(i+1, child, word):
                        return True
                return False
            else: # any alphabet
                if char not in curr.children:
                    return False
                else:
                    curr = curr.children[char]
        return curr.word # if word ends here
        
    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)