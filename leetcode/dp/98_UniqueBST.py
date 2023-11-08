class Solution(object):
    def numTrees(self, n):
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += (dp[j - 1] * dp[i - j])
        return dp[n]


class Solution(object):
    def numTrees(self, n):
        dp = [0] * (n + 1)

        def rec(idx):
            if idx <= 1:
                return 1
            if dp[idx] != 0:
                return dp[idx]

            res = 0
            for j in range(1, idx + 1):
                res += rec(j - 1) * rec(idx - j)
            dp[idx] = res
            return res

        return rec(n)

