class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        wordset = set(wordList) 
        que = deque([beginWord])
        dis = 0
        while que:
            dis += 1
            for i in range(len(que)):
                word = que.popleft()
                if word == endWord:
                    return dis 
                for nxt in self.getnexts(word):
                    if nxt not in wordset or nxt in visited:
                        continue 
                    que.append(nxt) 
                    visited.add(nxt) 
        return 0 

    def getnexts(self, word):
        words = []
        for i in range(len(word)):
            l, r = word[:i], word[i+1:]
            for c in "qwertyuiopasdfghjklzxcvbnm":
                if c == word[i]:
                    continue 
                words.append(l + c + r)
        return words