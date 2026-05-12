class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        start, end = 0, len(matrix)-1 
        while start + 1 < end:
            mid = start + (end - start )//2 
            if matrix[mid][0] < target:
                start = mid 
            elif matrix[mid][0] > target:
                end = mid 
            else:
                return True 
        row = -1  
        if matrix[end][0] <= target:
            row = end 
        elif matrix[start][0] <= target:
            row = start 
        else:
            return False 
        
        start, end = 0, len(matrix[0])-1 
        while start + 1 < end:
            mid = start + (end - start )//2 
            if matrix[row][mid] < target:
                start = mid 
            elif matrix[row][mid] > target:
                end = mid 
            else:
                return True 
        if matrix[row][start] == target:
            return True 
        return matrix[row][end] == target

