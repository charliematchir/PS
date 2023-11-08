class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        n, m = len(text1), len(text2)
        dp = [0] * (m + 1)

        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[m]

