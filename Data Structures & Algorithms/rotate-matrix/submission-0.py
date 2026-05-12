class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse the matrix vertically
        # matrix.reverse()
        n = len(matrix) 
        for i in range(n//2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
