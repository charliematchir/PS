class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        answer = 0

        # def dfs(y, x, prev):
        #     if y<0 or y>=m or x<0 or x>=n or prev >= matrix[y][x]:
        #         return 0
        #
        #     if dp[y][x] != -1:
        #         return dp[y][x]
        #
        #     res = 0
        #     res = max(res, 1+dfs(y+1, x, matrix[y][x]))
        #     res = max(res, 1+dfs(y-1, x, matrix[y][x]))
        #     res = max(res, 1+dfs(y, x+1, matrix[y][x]))
        #     res = max(res, 1+dfs(y, x-1, matrix[y][x]))
        #
        #     dp[y][x] = res
        #     return dp[y][x]
        #
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]



        if not matrix or not matrix[0]: return 0

        for i in range(m):
            for j in range(n):
                answer = max(answer, dfs(i, j))
        return answer