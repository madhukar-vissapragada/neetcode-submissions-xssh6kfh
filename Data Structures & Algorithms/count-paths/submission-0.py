class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(0, 0, m, n, {})

    def solve(self, current_row: int, current_column: int, row_size: int, column_size: int, memo: dict) -> int:
        if current_row == row_size - 1 and current_column == column_size - 1:
            return 1

        current_key = (current_row, current_column)
        if current_key in memo:
            return memo[current_key]

        move_right = move_down = 0
        if current_column + 1 < column_size:
            move_right = self.solve(current_row, current_column + 1, row_size, column_size, memo)
        if current_row + 1 < row_size:
            move_down = self.solve(current_row + 1, current_column, row_size, column_size, memo)

        result = move_right + move_down
        memo[current_key] = result
        return result

