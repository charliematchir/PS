from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1]:
            return -1

        q = deque([(0, 0)])
        answer = 1
        while q:
            size = len(q)
            for _ in range(size):
                yp, xp = q.popleft()
                if yp == n - 1 and xp == n - 1:
                    return answer
                for dy, dx in [(1, 1), (0, 1), (1, 0), (-1, 1), (1, -1), (-1, -1), (-1, 1), (-1, 0), (0, -1)]:
                    y = dy + yp
                    x = dx + xp

                    if y >= 0 and y < n and x >= 0 and x < n and grid[y][x] == 0:
                        grid[y][x] = 1
                        q.append((y, x))
            answer += 1

        return -1
