class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        session = []

        ######

        def solve(pos):
            if pos >= n:
                return 0
            session.append(tasks[pos])
            ans = 1 + solve(pos + 1)
            session.pop()

            for i in range(len(session)):
                if session[i] + tasks[pos] <= sessionTime:
                    session[i] += tasks[pos]
                    ans = min(ans, solve(pos + 1))
                    session[i] -= tasks[pos]
            return ans

        return solve(0)

        ######

        def dp(mask):
            if mask == 0: return (1, 0)
            ans = (float("inf"), float("inf"))
            for j in range(n):
                if mask & (1 << j):
                    pieces, last = dp(mask - (1 << j))
                    full = (last + tasks[j] > T)
                    ans = min(ans, (pieces + full, tasks[j] + (1 - full) * last))
            return ans

        return dp((1 << n) - 1)[0]



