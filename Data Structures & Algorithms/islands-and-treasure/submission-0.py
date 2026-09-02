from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        s = set()

        m = len(grid)
        n = len(grid[0])

        def queueAdjacents(row, col, distance):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dx, dy in directions:
                adjacentRow = row + dx
                adjacentCol = col + dy

                if adjacentRow >= m or adjacentRow < 0:
                    continue
                if adjacentCol >= n or adjacentCol < 0:
                    continue

                if grid[adjacentRow][adjacentCol] != 2147483647 or (adjacentRow, adjacentCol) in s:
                    continue
                
                q.append([adjacentRow, adjacentCol, distance + 1])
                s.add((adjacentRow, adjacentCol))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    queueAdjacents(row, col, 0)

        while q:
            row, cell, distance = q.popleft()
            grid[row][cell] = distance
            queueAdjacents(row, cell, distance)



