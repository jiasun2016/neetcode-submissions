class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s) 
        if not s:
            return 0 
        dp=[0]*3 
        dp[0] = 1 
        dp[1] = self.getdecode(s[0])
        for i in range(2, n+1):
            dp[i%3] =  dp[(i-1)%3] * self.getdecode(s[i-1:i]) +  dp[(i-2)%3] * self.getdecode(s[i-2:i]) 
        return dp[n%3]

    def getdecode(self, s): 
        if len(s) == 1 and s in "123456789":
            return 1 
        if len(s) == 2:
            if s[0] == '1':
                return 1
            if s[0] == '2' and s[1] in '0123456':
                return 1
            
        return 0
            