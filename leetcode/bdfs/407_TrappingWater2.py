from heapq import heappop, heappush


class Solution(object):
    def trapRainWater(self, height):

        m, n = len(height), len(height[0])
        if m <= 2 or n <= 2:
            return 0
        answer = 0
        heap = []
        height[0][0] = height[0][n - 1] = height[m - 1][0] = height[m - 1][n - 1] = -1
        for i in range(1, m - 1):
            heappush(heap, (height[i][0], (i, 0)))
            heappush(heap, (height[i][n - 1], (i, n - 1)))
            height[i][0] = height[i][n - 1] = -1

        for i in range(1, n - 1):
            heappush(heap, (height[0][i], (0, i)))
            heappush(heap, (height[m - 1][i], (m - 1, i)))
            height[0][i] = height[m - 1][i] = -1
        while heap:
            h, (yp, xp) = heappop(heap)
            for i, j in [(yp - 1, xp), (yp, xp - 1), (yp + 1, xp), (yp, xp + 1)]:
                if i < 0 or i >= m or j < 0 or j >= n or height[i][j] == -1:
                    continue
                answer += max(0, h - height[i][j])
                heappush(heap, (max(h, height[i][j]), (i, j)))
                height[i][j] = -1
        return answer