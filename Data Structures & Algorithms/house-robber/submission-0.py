class Solution:
    
     def rob(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)
            
        f = [0] * 3
        f[0], f[1] = A[0], max(A[0], A[1])
        
        for i in range(2, len(A)):
            f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + A[i])
            
        return f[(len(A) - 1) % 3]