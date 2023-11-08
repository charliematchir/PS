class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        total = sum(stones)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for w in stones:
            for i in range(target, w - 1, -1):
                dp[i] = dp[i] or dp[i - w]

        for i in range(target, -1, -1):
            if dp[i]:
                return total - 2 * i