class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False
        self.word = None 
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode() 
            curr = curr.children[c] 
        curr.isword = True 
        curr.word = word

    def find(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return None  
            curr = curr.children[c] 
        return curr

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        
        trie = Trie()
        for w in words:
            trie.add(w) 
        visited = set() 
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.add((i, j)) 
                c = board[i][j]
                self.search(
                    board, i, j,
                    trie.root.children.get(c),
                    res, visited)
                visited.remove((i,j))
        return list(res)
    def search(self, board, x, y, node, res, visited):
        DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if not node:
            return 
        if node.isword == True:
            res.add(node.word)
        for dx, dy in DIRECTIONS:
            nx, ny = dx+x, dy+y 
            if not self.isvalid(board, nx, ny, visited):
                continue 
            visited.add((nx, ny))
            c = board[nx][ny]
            self.search(
                    board, nx, ny,
                    node.children.get(c),
                    res, visited)
            visited.remove((nx, ny))
    def isvalid(self, board, x, y, visited):
        return 0 <= x < len(board) and 0<=y < len(board[0]) and (x, y) not in visited


        