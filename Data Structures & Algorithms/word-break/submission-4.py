class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True 
        if not wordDict:
            return False 
        n = len(s)
        dp = [False]*(n+1) 
        dp[0] = True
        wordSet = set(wordDict)
        maxLen = max([ len(word) for word in wordDict ])  
        for i in range(1, n+1):
            for l in range(1, maxLen+1):
                if i < l:
                    break 
                word = s[i-l:i]
                if word in wordDict:
                    dp[i] = dp[i] or dp[i-l] 
                    
        return dp[n]
