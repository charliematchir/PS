from heapq import heappop, heappush
from collections import defaultdict
INF = 987654321

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        ############### BFS ####################
        # graph = defaultdict(dict)
        # dist =  [INF]*n
        # dist[src] = 0
        # q = deque([(0, src)])

        # for fr,to,cost in flights:
        #     graph[fr][to] = cost

        # step = 0
        # while q and step <= k:
        #     l = len(q)
        #     for _ in range(l):
        #         cost, node = q.pop()
        #         if node not in graph:
        #             continue
        #         for n, c in graph[node].items():
        #             if dist[n] > c+cost:
        #                 dist[n] = c+cost
        #                 q.append((c+cost, n))
        #     step += 1
        # return dist[dst] if dist[dst] != INF else -1

        ############### DIJKSTRA ####################
        graph = defaultdict(dict)
        stops = [-1] * n
        pq = [(0, src, k + 1)]

        for fr, to, cost in flights:
            graph[fr][to] = cost

        while pq:
            cost, node, steps = heappop(pq)

            if node == dst:
                return cost

            if steps < stops[node] or steps <= 0:
                continue

            stops[node] = steps

            # if node not in graph:
            #     continue
            for to in graph[node]:
                heappush(pq, (cost + graph[node][to], to, steps - 1))
        return -1
