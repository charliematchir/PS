class Solution(object):
    def minimumEffortPath(self, h):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        row, col = len(h), len(h[0])
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[False] * col for _ in range(row)]
        global answer
        answer = 1000000

        # dq = deque([(0,0)])
        # while dq:
        #     size = len(dq)
        #     for _ in range(size):
        #         r, c = dq.popleft()
        #         for yp, xp in dir:
        #             y, x = r+yp, c+xp
        #             if y>=row or y<0 or x>=col or x<0:
        #                 continue
        #             if not visited[y][x]:
        #                 if

        #         dq.append((y,x))

        #     e = max(e, abs(prev- h[r][c]))

        def dfs(e, prev, r, c):
            e = max(e, abs(prev - h[r][c]))
            global answer
            if e >= answer:
                return
            if r == row - 1 and c == col - 1:
                # global answer
                answer = min(answer, e)
                return
            for yp, xp in dir:
                y, x = r + yp, c + xp
                if y >= row or y < 0 or x >= col or x < 0:
                    continue
                if not visited[y][x]:
                    visited[y][x] = True
                    dfs(e, h[r][c], y, x)
                    visited[y][x] = False

        dfs(0, h[0][0], 0, 0)
        return answer






