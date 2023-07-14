import sys
import heapq
from collections import defaultdict

def dijkstra_brute(G, V, src):
    dist = [float('inf')] * (V + 1)
    dist[src] = 0

    for i in range(1, V + 1):
        dist[i] = min(G[src][i], dist[i])
        if i != src:
            temp = i
            for j in range(1, V + 1):
                dist[j] = min(G[temp][j] + dist[temp], dist[j])
    print(dist[1:])

def dijkstra_graph(G, V, src):
    dist = [float('inf')] * (V + 1)
    dist[src] = 0

    visited = set()
    n = len(G)

    while len(visited) < n:
        min_d = float('inf')
        nxt = None

        for k, v in G[src].items():
            if k not in visited:
                dist[k] = min(dist[k], dist[src] + v)

            if k in G and dist[k] < min_d:
                min_d = dist[k]
                nxt = k
        if nxt is None:
            break
        visited.add(src)
        src = nxt

def dijkstra_pq(G,V,src):
    dist = {node: float('inf') for node in range(1, V+1)}
    dist[src] = 0
    pq = [(0, src)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_node not in G or curr_dist > dist[curr_node]:
            continue

        for node, weight in G[curr_node].items():
            distance = curr_dist + weight
            if distance < dist[node]:
                dist[node] = distance
                heapq.heappush(pq, (distance, node))

    print(dist)

def main():
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())

    ### for brute force ###
    # W = [[float('inf')] *(V+1) for _ in range(V+1)]
    # for _ in range(E):
    #     u, v, w = map(int, sys.stdin.readline().split())
    #     W[u][v] = w

    graph = defaultdict(dict)
    # graph = {node: {} for node in range(1,V+1)}
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        if v not in graph[u]:
            graph[u][v] = w
        else:
            graph[u][v] = min(graph[u][v], w)


    print(graph)
    dijkstra_pq(graph,V,K)



if __name__ == '__main__':
    main()
#
# import sys
# import heapq
# import math
#
# V, E = map(int, sys.stdin.readline().split())
# K = int(sys.stdin.readline())
#
# graph = {node: {} for node in range(1, V + 1)}
#
# for _ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     graph[u][v] = w
#
# dist = [float('inf')] * (V + 1)
# dist[K] = 0
#
# pq = []
# heapq.heappush(pq, (0, K))
#
# while pq:
#     curr_dist, curr_node = heapq.heappop(pq)
#     if curr_dist > dist[curr_node]:
#         continue
#
#     for node, weight in graph[curr_node].items():
#         distance = curr_dist + weight
#         if distance < dist[node]:
#             dist[node] = distance
#             heapq.heappush(pq, (distance, node))
#
# for i in dist[1:]:
#     print(i if i != float('inf') else "INF")