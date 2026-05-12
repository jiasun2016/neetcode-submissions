class TrieNode:
    def __init__(self):
        self.children = {}
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
        
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
               
                c = board[i][j]
                board[i][j] = "#"
                self.search(
                    board, i, j,
                    trie.root.children.get(c),
                    res, )
                board[i][j] = c
               
        return list(res)
    def search(self, board, x, y, node, res):
        DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if not node:
            return 
        if node.word:
            res.append(node.word)
            node.word = None 
        for dx, dy in DIRECTIONS:
            nx, ny = dx+x, dy+y 
            if not self.isvalid(board, nx, ny):
                continue 
            c = board[nx][ny]
            board[nx][ny] = "#"
            self.search(
                    board, nx, ny,
                    node.children.get(c),
                    res)
            board[nx][ny] = c

    def isvalid(self, board, x, y):
        return 0 <= x < len(board) and 0<=y < len(board[0]) and board[x][y] != "#"


        