DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
class TrieNode:			
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):		
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()   
            node = node.children[c]     		
        node.is_word = True
        node.word = word     
    def find(self, word):	
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return [] 
        trie = Trie() 

        for w in words:
            trie.add(w)
        
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c= board[i][j] 
                self.search(board, i, j, trie.root.children.get(c), set([(i,j)]), res)
        return list(res)

    def search(self, board, x, y, node, visited, res):
        if not node:
            return 
        if node.is_word:
            res.add(node.word) 
        for delta_x, delta_y in DIRECTIONS:			
            x_ = x + delta_x
            y_ = y + delta_y
            if not self.inside(board, x_, y_):
                continue
            if (x_, y_) in visited:
                continue
            visited.add((x_, y_)) 
            self.search(board, x_, y_, node.children.get(board[x_][y_]), visited, res) 
            visited.remove((x_, y_)) 

    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

