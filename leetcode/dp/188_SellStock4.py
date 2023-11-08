class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0

        # dp = [[0] * n for _ in range(k + 1)]
        # for t in range(1, k+1):
        #     for i in range(1, n):
        #         minimum = prices[0]
        #         for j in range(1, i+1):
        #             minimum = min(minimum, prices[j] - dp[t - 1][j - 1])
        #         dp[t][i] = max(prices[i] - minimum, dp[t][i - 1])
        # return dp[k][n-1]

        # dp = [0] * n
        # for _ in range(k):
        #     minimum = prices[0]
        #     temp = dp[0]
        #     for i in range(1, n):
        #         minimum = min(minimum, prices[i] - temp)
        #         temp = dp[i]
        #         dp[i] = max(prices[i] - minimum, dp[i - 1])
        # return dp[n-1]

        # dp 는 sell
        # minimum은 buy
        dp = [0] * (k+1)
        minimum = [prices[0]] * (k+1)
        for i in range(1, n):
            for t in range(1, k+1):
                minimum[t] = min(minimum[t], prices[i] - dp[t-1])
                dp[t] = max(prices[i] - minimum[t], dp[t])
        return dp[k]
