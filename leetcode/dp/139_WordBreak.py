class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        # n = len(s)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # for i in range(n):
        #     if dp[i] == False:
        #         continue
        #     for w in wordDict:
        #         if len(w) <= n-i and s[i: i + len(w)]== w:
        #             dp[i + len(w)] = True

        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if len(w) + i <= n and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]
