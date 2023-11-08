class Solution(object):
    def isMatch(self, s, p):
        n, m = len(s), len(p)
        if n == 0 and m == 0:
            return True
        dp = [[0]* (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if j > i:
                    if p[j] == '*':
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 0
                        # if p[j] == '?' or s[i] == p[j]:
                        #     dp[i][j] = dp[i][j-1]
                        # else:
                        #     dp[i][j] = 0
                else:
                    if p[j] == '*':
                        dp[i][j] = dp[i][j-1]
                    elif p[j] == '?' or s[i]==p[j]:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = 0


