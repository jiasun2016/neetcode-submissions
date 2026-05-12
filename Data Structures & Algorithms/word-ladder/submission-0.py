class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        visited = set()
        wordSet = set(wordList)
        
        queue = collections.deque([beginWord]) 
        visited.add(beginWord)
        lens = 0
        while queue:
            lens += 1 
            for i in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return lens 
                for nxt in self.getNexts(node):
                    
                    if nxt not in wordSet or nxt in visited:
                        continue 
                    print(nxt)
                    visited.add(nxt)
                    queue.append(nxt) 
        return 0 

    def getNexts(self, node):
        words = [] 
        for i in range(len(node)):
            left, right = node[:i],  node[i+1:]
            for c in "qwertyuiopasdfghjklzxcvbnm":
                if c == node[i]:
                    continue 
                words.append(left + c + right) 
        return words