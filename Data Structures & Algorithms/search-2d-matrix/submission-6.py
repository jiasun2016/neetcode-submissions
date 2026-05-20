class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols -1 
        while l + 1 < r:
            mid = l + (r-l)//2 
            row, col = mid//cols, mid%cols
            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] > target:
                r = mid 
            else:
                l = mid 
        
        if matrix[l//cols][l%cols] == target:
            return True 
        return matrix[r//cols][r%cols] == target