import heapq
INF = 987654321
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = {}
            graph[u][v] = w

        dists = [INF] * (n + 1)
        dists[k] = 0
        pq = [(0, k)]

        while pq:
            dist, node = heapq.heappop(pq)

            if node not in graph or dist > dists[node]:
                continue

            for neighbor, d in graph[node].items():
                distance = d + dist
                if dists[neighbor] > distance:
                    dists[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        answer = 0

        for v in dists[1:]:
            if v == INF:
                return -1
            answer = max(answer, v)
        return answer
