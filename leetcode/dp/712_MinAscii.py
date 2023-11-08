class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        # n, m = len(s1), len(s2)
        # dp = [[0]*(m+1) for _ in range(n+1)]

        # for i in range(m-1, -1, -1):
        #     dp[n][i] = dp[n][i+1] + ord(s2[i])
        # for i in range(n-1, -1, -1):
        #     dp[i][m] = dp[i+1][m] + ord(s1[i])

        # for i in range(n-1, -1, -1):
        #     for j in range(m-1, -1, -1):
        #         if s1[i] == s2[j]:
        #             dp[i][j] = dp[i+1][j+1]
        #         else:
        #             dp[i][j] = min(ord(s1[i]) + dp[i+1][j], ord(s2[j]) + dp[i][j+1])

        # return dp[0][0]

        n1, n2 = len(s1), len(s2)
        dp = [0] * (n1 + 1)
        for i in range(n2):
            prev = dp[0]
            for j in range(n1):
                tmp = dp[j + 1]
                if s2[i] == s1[j]:
                    dp[j + 1] = prev + ord(s1[j])
                else:
                    dp[j + 1] = max(dp[j], dp[j + 1])
                prev = tmp
        return sum(ord(x) for x in s1) + sum(ord(y) for y in s2) - 2 * max(dp)
