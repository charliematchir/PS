from collections import deque


class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        if m <= 2 or n <= 2:
            return 0

        answer = 0

        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = 0
            while q:
                yp, xp = q.popleft()
                for y, x in [(yp - 1, xp), (yp + 1, xp), (yp, xp - 1), (yp, xp + 1)]:
                    if y >= m or y < 0 or x < 0 or x >= n:
                        continue
                    if grid[y][x] == 1:
                        q.append((y, x))
                        grid[y][x] = 0

        for i in range(m):
            if grid[i][0] == 1:
                bfs(i, 0)

            if grid[i][n - 1]:
                bfs(i, n - 1)

        for j in range(n):
            if grid[0][j] == 1:
                bfs(0, j)

            if grid[m - 1][j]:
                bfs(m - 1, j)
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1:
                    answer += 1
        return answer

        # for i in range(1, m-1):
        #     for j in range(1, n-1):
        #         if grid[i][j] == 1:
        #             q = deque([(i,j)])
        #             flag = False
        #             num = 1
        #             grid[i][j] = 0
        #             while q:
        #                 yp, xp = q.popleft()
        #                 for y, x in [(yp-1, xp), (yp+1, xp), (yp, xp-1), (yp,xp+1)]:
        #                     if y >= m or y < 0 or x < 0 or x >= n:
        #                         continue

        #                     if grid[y][x] == 1:
        #                         if y == m-1 or y == 0 or x == 0 or x == n-1:
        #                             flag = True
        #                         grid[y][x] = 0
        #                         q.append((y,x))
        #                         num += 1

        #             if not flag:
        #                 answer += num
        # return answer



