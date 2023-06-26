import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 987654321

def main():
    N, M, X = map(int, input().split())
    graph = {}
    rev_graph = {}
    for _ in range(M):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = {}
        if v not in rev_graph:
            rev_graph[v] = {}

        graph[u][v] = w
        rev_graph[v][u] = w

    answer = 0
    dist_to_X, dist_from_X = dijkstra(rev_graph, N, X), dijkstra(graph, N, X)

    for i in range(1, N+1):
        answer = max(answer, dist_from_X[i]+dist_to_X[i])
    print(answer)


def dijkstra(graph, n, src):

    distance = [INF] * (n+1)
    distance[src] = 0
    pq = [(0, src)]

    while pq:
        d, node = heappop(pq)

        if node not in graph or d > distance[node]:
            continue

        for neighbor, di in graph[node].items():
            dist = d + di
            if dist < distance[neighbor]:
                distance[neighbor] = dist
                heappush(pq, (dist, neighbor))

    return distance


if __name__ == '__main__':
    main()
