class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        rows = len(matrix)
        cols = len(matrix[0])
        l, r =0, rows-1
        while l + 1<r:
            mid = l + (r-l)//2
            if matrix[mid][0] == target:
                return True 
            if matrix[mid][0] > target:
                r = mid 
            else:
                l = mid 
        row = -1
        if matrix[r][0] <= target:
            row  = r
        elif matrix[l][0] <= target:
            row = l 
        else:
            return False 
        l, r =0, cols-1
        while l + 1<r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True 
            if matrix[row][mid] > target:
                r = mid
            else:
                l = mid 
        if matrix[row][l] == target:
            return True 
        return matrix[row][r] == target