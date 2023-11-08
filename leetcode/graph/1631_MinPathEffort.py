from heapq import heappop, heappush

class Solution(object):
    def minimumEffortPath(self, heights):

        row, col = len(heights), len(heights[0])
        h = [(0, (0, 0))]
        dist = [[float('inf')] * col for _ in range(row)]
        dist[0][0] = 0

        while h:
            e, (yp, xp) = heappop(h)
            if yp == row - 1 and xp == col - 1:
                return dist[yp][xp]

            for y, x in [(yp + 1, xp), (yp, xp + 1), (yp, xp - 1), (yp - 1, xp)]:
                if y < 0 or x < 0 or y >= row or x >= col:
                    continue

                v = max(e, abs(heights[yp][xp] - heights[y][x]))
                if v < dist[y][x]:
                    dist[y][x] = v
                    heappush(h, (dist[y][x], (y, x)))
        return 0