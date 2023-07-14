# ######## Check Negative Cycle ########
#
# # class Solution:
# #     def isNegativeWeightCycle(self, n, graph):
# #         src = 0
# #         distance = [INF] * n
# #         distance[src] = 0
#
# #         for _ in range(n - 1):
# #             for u, v, weight in graph:
# #                 if distance[u] + weight < distance[v]:
# #                     distance[v] = distance[u] + weight
# #
# #         for u, v, weight in graph:
# #             if distance[u] + weight < distance[v]:
# #                 return 1
# #         return 0
#
#
# def bellman_ford(graph, source, dst):
#     n = len(graph)
#     distance = [float('inf')] * n
#     distance[source] = 0
#
#     # Relax edges repeatedly
#     for _ in range(n - 1):
#         # 위의 for loop 이 한번 돌고 난 뒤의 distance의 의미는
#         # src 에서 한 edge 만큼 거리에 있는 v들까지의 거리
#         # 여기서 주의할게, 한번 만에 이동할 수 있는 v들의 dist가 아닌,
#         # src 의 neigbor들의 dist인거임.
#
#         # 그리고 중간의 distance 값들은 최단거리임을 보장하지 않음.
#
#         for u, v, weight in graph:
#             if distance[u] == float('inf'):
#                 continue
#             if distance[u] + weight < distance[v]:
#                 distance[v] = distance[u] + weight
#
#     # Check for negative cycles
#     for u, v, weight in graph:
#         if distance[u] != float('inf') and distance[u] + weight < distance[v]:
#             return -1  # Negative cycle detected
#
#     return distance[dst]


import sys
from collections import defaultdict
input = sys.stdin.readline

def bellman_ford(graph, n):
    distance = [float('inf')] * (n + 1)
    distance[1] = 0

    for i in range(1, n+1):
        # if distance[i] == float('inf'):
        #     continue
        for k in graph:
            if distance[k] == float('inf'):
                continue
            for v, w in graph[k].items():
                if distance[i] + w < distance[v]:
                    distance[v] = distance[i] + w

    for k in graph:
        for v, w in graph[k].items():
            if distance[k] == float('inf'):
                continue
            if distance[k] + w < distance[v]:
                return [-1]
    return distance[2:]

def main():
    N, M = map(int, input().split())

    g = defaultdict()

    # graph = [dict() for _ in range(N + 1)]
    graph = defaultdict(defaultdict)
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u][v] = min(graph[u].get(v, float('inf')), w)

    dist = bellman_ford(graph, N)

    if dist == [-1]:
        print(-1)
    else:
        for v in dist:
            print(v if v != float('inf') else -1)



if __name__ == '__main__':
    main()