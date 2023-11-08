class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        length = len(strs)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for st in strs:
            one = st.count('1')
            zero = len(st) - one
            for ones in range(n, -1, -1):
                for zeros in range(1, n + 1):
                    if one <= ones and zero <= r_zero:
                        dp[count][ones] = max(1 + dp[count - 1][ones - one], dp[count - 1][ones])
                    else:
                        dp[count][ones] = dp[count - 1][ones]

