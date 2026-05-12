DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]  
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0  
        sequence = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sequence.append((matrix[i][j], i, j))  

        sequence.sort()
        check = {} 
        for h, x, y in sequence:  
            cur_pos = (x, y)
            if cur_pos not in check:
                check[cur_pos] = 1  
            cur_path = 0
            for dx, dy in DIRECTIONS:
                if self.is_valid(x+dx, y+dy, matrix, h):
                    cur_path = max(cur_path, check[(x+dx, y+dy)])  
            check[cur_pos] += cur_path 
        return max(check.values()) 

    def is_valid(self, x, y, matrix, h):
        row, col = len(matrix), len(matrix[0])
        # 合法且更小
        return 0 <= x < row and 0 <= y < col and matrix[x][y] < h  
