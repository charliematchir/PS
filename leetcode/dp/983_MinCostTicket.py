from collections import defaultdict


class Solution(object):
    def mincostTickets(self, days, costs):
        n = days[-1]
        dp = defaultdict(int)
        day = set(days)
        for i in range(1, n + 1):
            if i not in day:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[i - 1] + costs[0], dp[i - 7] + costs[1], dp[i - 30] + costs[2])
        return dp[n]

