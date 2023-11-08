class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ################ DP #################
        if s == s[::-1]:
            return s

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        length, st, ed = 0, 0, 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i<=1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i >= length:
                            length = j-i
                            st, ed = i, j
        return s[st:ed+1]
        ######################################


        ################ Two Pointer #################
        n = len(s)
        m_len = 0
        st, ed = 0, 0

        for i in range(n):
            # odd
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l-2 >= m_len:
                m_len, st, ed = r - l - 2, l + 1, r - 1

            # even
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - l - 2 >= m_len:
                m_len, st, ed = r - l - 2, l + 1, r - 1

        return s[st:ed + 1]
        ######################################
