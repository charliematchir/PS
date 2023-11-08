class Solution(object):
    def minDistance(self, word1, word2):

        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]

        l1, l2 = len(word1), len(word2)
        tbl = [0] * (l2 + 1)

        for i in range(l1):
            old = list(tbl)
            for j in range(l2):
                if word1[i] == word2[j]:
                    tbl[j + 1] = old[j] + 1
                else:
                    tbl[j + 1] = max(tbl[j], tbl[j + 1])

        return l1 + l2 - 2 * tbl[l2]

        n, m = len(word1), len(word2)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = 1 + dp[j - 1]
                else:
                    cur[j] = max(dp[j], cur[j - 1])
            dp = cur

        common = dp[m]
        return (n - common) + (m - common)