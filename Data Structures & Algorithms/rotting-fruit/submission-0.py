from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # start all rotten fruits
        # push all fresh fruit adjacents onto queue and mark as seen
        # repeat until queue is empty
        # track the number of minutes for each fruit with rotten ones at 0

        # if the number of items pushed onto the queue is less than the total number of fresh fruits
        # return -1

        m = len(grid)
        n = len(grid[0])

        q = deque()
        s = set()

        fresh = 0
        rotted = 0
        time = 0

        def add_neighbors(row, col, minutes):
            nonlocal rotted

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < m and 0 <= new_col < n:
                    if grid[new_row][new_col] == 1 and (new_row, new_col) not in s:
                        q.append((new_row, new_col, minutes + 1))
                        s.add((new_row, new_col))
                        rotted += 1

        # initialize board
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh += 1
                    continue
                
                if grid[row][col] == 2:
                    q.append((row, col, 0))

        while q:
            row, col, minutes = q.popleft()
            time = minutes
            add_neighbors(row, col, minutes)

        return time if fresh == rotted else -1
