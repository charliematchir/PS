import collections

class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = collections.defaultdict(int)
        dp[-1] = questions[-1][0]
        for i in range(n-1, -1, -1):
            dp[i] = max(questions[i][0] + dp[i+questions[i][1]+1], dp[i+1])
        return dp[0]
