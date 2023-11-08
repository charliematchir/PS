class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        for i in range(3, n):
            dp[i] = (2 * dp[i - 1] + dp[i - 3])
        return dp[-1] % 1000000007