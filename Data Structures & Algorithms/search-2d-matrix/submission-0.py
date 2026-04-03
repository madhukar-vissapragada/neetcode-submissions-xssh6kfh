class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        total_elements = len(matrix) * (len(matrix[0]))
        low = 0 
        high = total_elements - 1 
        cols = len(matrix[0])

        while low <= high: 
            mid = (low + high) // 2

            row = mid // cols
            col = mid % cols 
            element = matrix[row][col]

            if element == target:
                return True

            if element > target:
                high = mid - 1 
            else:
                low = mid + 1
        
        return False 



    
        