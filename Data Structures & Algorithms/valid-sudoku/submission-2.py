class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check the rows
        for row in range(9):
            seen = set()

            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # Check the columns
        for col in range(9):
            seen = set()

            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # Check the sub-squares
        for row, col in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
            seen = set()

            for i in range(3):
                for j in range(3):
                    nrow, ncol = row + i, col + j
                    if board[nrow][ncol] == ".":
                        continue
                    if board[nrow][ncol] in seen:
                        return False
                    
                    seen.add(board[nrow][ncol])

        return True

