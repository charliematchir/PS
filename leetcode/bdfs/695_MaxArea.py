class Solution(object):
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid[0])
        dq = collections.deque()
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = area = 0
                    dq.append((i,j))
                    while dq:
                        yp, xp = dq.popleft()
                        area += 1
                        for y, x in [(yp-1, xp), (yp+1,xp), (yp, xp-1), (yp, xp+1)]:
                            if y < 0 or y >= m or x < 0 or x >= n or grid[y][x] == 0:
                                continue
                            grid[y][x] = 0
                            dq.append((y,x))
                    answer = max(answer, area)

        return answer