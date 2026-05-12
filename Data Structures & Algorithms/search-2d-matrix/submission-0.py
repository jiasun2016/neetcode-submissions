class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix) or (not matrix[0]):
            return False 
        rows, cols = len(matrix), len(matrix[0])
        start = 0
        end = rows * cols -1  
        while start + 1 < end:
            mid = start + (end-start)//2 
            val = matrix[mid//cols][mid%cols]
            if val == target:
                return True
            elif val > target:
                end = mid 
            else:
                start = mid  
            
        if matrix[start//cols][start%cols] == target:
            return True 
        if matrix[end//cols][end%cols] == target:
            return True  
        return False