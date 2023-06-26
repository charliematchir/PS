import sys
import heapq

INF = 987654321

def dijkstra(g, n, src, nxt):
    dist = [INF] * (n+1)
    dist[src] = 0

    pq = [(0, src)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > dist[curr_node]:
            continue

        if curr_node in g:
            for node, weight in g[curr_node].items():
                distance = curr_dist + weight
                if distance < dist[node]:
                    dist[node] = distance
                    heapq.heappush(pq, (distance, node))
    if dist[1] == INF or dist[nxt] == INF or dist[n] == INF:
        return None
    else:
        return dist
#
#
# ans1 = dijkstra(graph, V, v1, v2)
# ans2 = dijkstra(graph, V, v2, v1)
# print(min(ans1, ans2))


def main():

    V, E = map(int, sys.stdin.readline().split())

    graph = {}
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = w
        graph[v][u] = w

    v1, v2 = map(int, sys.stdin.readline().split())
    dist1 = dijkstra(graph, V, v1, v2)
    dist2 = dijkstra(graph, V, v2, v1)

    if dist1 is None or dist2 is None:
        print(-1)
    else:
        ans1 = dist1[1] + dist1[v2] + dist2[V]
        ans2 = dist2[1] + dist2[v1] + dist1[V]
        print(min(ans1, ans2))


if __name__ == '__main__':
    main()