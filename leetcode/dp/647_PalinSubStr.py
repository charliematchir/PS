class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        answer = n
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i <= 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        answer += 1
        return answer




