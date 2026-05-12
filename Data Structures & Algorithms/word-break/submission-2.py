class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True 
        if not wordDict:
            return False 
        n = len(s)
        dp = [False]*(n+1) 
        dp[0] = True
        maxLen = max([ len(word) for word in wordDict ])  
        for i in range(n+1):
            for l in range(1, maxLen+1):
                if i < l:
                    break 
                word = s[i-l:i]
                if dp[i-l] and word in wordDict:
                    dp[i] = True 
                    break
        return dp[n]
