import sys
import heapq
from collections import defaultdict
INF = 987654321

def dp(g, e):
    dist = [INF] * (e+1)
    dist[0] = 0
    if 0 in g:
        for key, val in g[0].items():
            dist[key] = min(min(val), dist[key])

    for i in range(1, e+1):
        dist[i] = min(dist[i-1]+1, dist[i])
        if i in g:
            for key, val in g[i].items():
                dist[key] = min(min(val)+dist[i], dist[key])
    return dist[e]

def main():

    V, E = map(int, sys.stdin.readline().split())
    graph = defaultdict(lambda: defaultdict(list))

    for _ in range(V):
        u, v, w = map(int, sys.stdin.readline().split())
        if v-u <= w or v > E:
            continue
        graph[u][v].append(w)


if __name__ == '__main__':
    main()
#
# import sys
#
# N, D = map(int, input().split())
# arr = [i for i in range(D+1)]
# sc = [list(map(int, input().split())) for _ in range(N)]
#
# for i in range(D+1):
#     arr[i] = min(arr[i-1]+1, arr[i])
#     for s, e, shortcut in sc:
#         if i == s and e <= D and arr[i]+shortcut < arr[e]:
#             arr[e] = arr[i]+shortcut
# print(arr[D])