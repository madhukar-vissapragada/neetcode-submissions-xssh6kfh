class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        result = 0
        rows = len(matrix)
        cols = len(matrix[0])
        memo = {}
        for row in range(rows):
            for col in range(cols):
                result = max(result, self.solve(matrix, row, col, -1, rows, cols, memo))
        
        return result
    
    def solve(self, matrix: List[List[int]], row: int, col: int, prev_index: int, rows: int, cols: int, memo: dict) -> int:
        if row not in range(0, rows):
            return 0 
        if col not in range(0, cols):
            return 0
        

        current_key = (row, col, prev_index)
        if current_key in memo:
            return memo[current_key]
        
        result = 0
        move_left = move_right = move_top = move_down = 0
        if prev_index == -1 or matrix[prev_index[0]][prev_index[1]] < matrix[row][col]:
            move_left = 1 + self.solve(matrix, row, col - 1, (row, col), rows, cols, memo)
            move_top = 1 + self.solve(matrix, row - 1, col, (row, col), rows, cols, memo)
            move_right = 1 + self.solve(matrix, row, col + 1, (row, col), rows, cols, memo)
            move_down = 1 + self.solve(matrix, row + 1, col, (row, col), rows, cols, memo)
        
        result = max(max(move_left, move_right), max(move_top, move_down))
        memo[current_key] = result
        return result 
