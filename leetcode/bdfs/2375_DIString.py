class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """

        # self.ans = float('inf')
        # visited = [False] * 10
        # n = len(pattern)
        #
        # def dfs(value, idx):
        #     if idx >= n:
        #         self.ans = min(self.ans, value)
        #         return str(self.ans)
        #
        #     if pattern[idx] == 'I':
        #         for i in range(value % 10 + 1, 10):
        #             if not visited[i]:
        #                 visited[i] = True
        #                 dfs(value * 10 + i, idx + 1)
        #                 visited[i] = False
        #
        #     else:
        #         for i in range(1, value % 10):
        #             if not visited[i]:
        #                 visited[i] = True
        #                 dfs(value * 10 + i, idx + 1)
        #                 visited[i] = False
        #     return
        #
        # for i in range(1, 10):
        #     visited[i] = True
        #     dfs(i, 0)
        #     visited[i] = False
        #     if self.ans != float('inf'):
        #         return str(self.ans)
        # return str(self.ans)

        res, stack = [], []
        for idx, char in enumerate(pattern + 'I', 1):
            stack.append(idx)
            if char == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(map(str, res))