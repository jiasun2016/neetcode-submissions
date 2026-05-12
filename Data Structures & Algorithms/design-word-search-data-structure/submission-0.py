
class TrieNode:
    def __init__(self):
        self.isword = False 
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() 
            curr = curr.children[c] 
        curr.isword = True 
        
    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)

    def dfs(self, index, word, root):
        curr = root 
        for i in range(index, len(word)):
            c = word[i]
            if c == ".": 
                for child in curr.children:
                    if self.dfs(i + 1, word, curr.children[child]):
                        return True 
                return False  
            else:
                if c not in curr.children:
                    return False
                curr =  curr.children[c]
        return curr.isword
     
