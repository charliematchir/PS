class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if s == s[::-1]:
            return n

        dp = [1] * n

        for i in range(n-1, -1, -1):
            prev = 0
            for j in range(i+1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
        return dp[-1]