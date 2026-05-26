class WordDictionary:

    def __init__(self):
        self.pt = PrefixTree()

    def addWord(self, word: str) -> None:
        self.pt.insert(word)
        
    def search(self, word: str) -> bool:
        return self.pt.search(word)
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() 
            curr = curr.children[c] 
        curr.isWord = True

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)
        
    def dfs(self, index, word, root):
        curr = root
        for i in range(index, len(word)):
            c = word[i]
            if c == ".":
                for child in curr.children:
                    if self.dfs(i+1, word, curr.children[child]):
                        return True 
                return False 
            elif c in curr.children:
                curr = curr.children[c]
            else:
                return False 
        return curr.isWord 


    def startsWith(self, prefix: str) -> bool:
        curr = self.root 
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False 
        return True
        
        
class TrieNode:
    def __init__(self):
        self.isWord = False 
        self.children = {}