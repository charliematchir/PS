import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = 987654321

def main():
    N, M = map(int, input().split())
    visible = list(map(int, input().split()))
    visible[-1] = 0
    graph = {}
    for _ in range(M):
        u, v, w = map(int, input().split())

        if visible[u] or visible[v]:
            continue
        # if (v != N-1 and visible[v] == 1) or (u != N-1 and visible[u] == 1):
        #     continue

        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}

        graph[v][u] = w
        graph[u][v] = w

    print(dijkstra(graph, N))


def dijkstra(graph, n):

    distance = [INF] * 10*7+1
    distance[0] = 0
    pq = [(0, 0)]

    while pq:
        d, node = heappop(pq)

        if node not in graph or d > distance[node]:
            continue

        if node == n-1:
            break

        for neighbor, di in graph[node].items():
            dist = d + di
            if dist < distance[neighbor]:
                distance[neighbor] = dist
                heappush(pq, (dist, neighbor))

    return distance[n-1] if distance[n-1] != INF else -1

if __name__ == '__main__':
    main()
