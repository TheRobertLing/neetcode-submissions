class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW_COUNT = len(board)
        COL_COUNT = len(board[0])

        not_surrounded = set()

        def searchRegion(startRow, startCol):
            seen = {(startRow, startCol)}
            queue = [(startRow, startCol)]
            is_surrounded = True

            while queue:
                r, c = queue.pop()

                if (r == 0 or r == ROW_COUNT - 1) or (c == 0 or c == COL_COUNT - 1):
                    is_surrounded = False
                
                for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROW_COUNT and 0 <= nc < COL_COUNT:
                        cell = board[nr][nc]

                        if cell == 'O' and (nr, nc) not in seen:
                            queue.append((nr, nc))
                            seen.add((nr, nc))
            
            
            if is_surrounded:
                for row, col in seen:
                    board[row][col] = 'X'
            else:
                not_surrounded.update(seen)


        for row in range(ROW_COUNT):
            for col in range(COL_COUNT):
                cell = board[row][col]
                if cell == 'O' and cell not in not_surrounded:
                    searchRegion(row, col)
                    
