class Solution(object):
    def findMaxFish(self, grid):

        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            answer = grid[i][j]
            grid[i][j] = 0
            for y, x in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                answer += dfs(y, x)
            return answer

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        return ans