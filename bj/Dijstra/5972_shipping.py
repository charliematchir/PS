import sys
import heapq
from collections import defaultdict

def dijkstra_pq(G,V,src,dst):
    dist = {node: float('inf') for node in range(1, V+1)}
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_node not in G:
            continue

        if curr_dist > dist[curr_node]:
            continue

        for node, weight in G[curr_node]:
            distance = curr_dist + weight
            if distance < dist[node]:
                dist[node] = distance
                heapq.heappush(pq, (distance, node))

    return dist[dst]

def main():
    V = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    graph = defaultdict(list)

    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
    src, dst = map(int, sys.stdin.readline().split())

    print(dijkstra_pq(graph,V,src, dst))

if __name__ == '__main__':
    main()
#
# import sys
# from heapq import heappop, heappush
#
# input = sys.stdin.readline
# INF = sys.maxsize
#
#
# def dijkstra(graph, start, end, n):
#     q = []
#     inD = [INF] * (n + 1)
#     heappush(q, (0, start))
#
#     while q:
#         cost, node = heappop(q)
#         if inD[node] < cost:
#             continue
#
#         if node == end:
#             break
#
#         for n_node, n_cost in graph[node].items():
#             n_cost += cost
#             if inD[n_node] > n_cost:
#                 inD[n_node] = n_cost
#                 heappush(q, (n_cost, n_node))
#     print(inD[end])
#
#
# def main():
#     N = int(input())
#     M = int(input())
#
#     graph = [dict() for _ in range(N + 1)]
#     for _ in range(M):
#         s, e, cost = map(int, input().split())
#         if e in graph[s]:
#             graph[s][e] = min(graph[s][e], cost)
#         else:
#             graph[s][e] = cost
#
#     start, end = map(int, input().split())
#     dijkstra(graph, start, end, N)
#
#
# main()