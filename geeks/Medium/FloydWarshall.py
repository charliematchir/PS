INF = 987654321


def floyd(graph):
    V = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])


def main():
    g= {{0,   5,  INF, 10},
        {INF,  0,  3,  INF},
        {INF, INF, 0,   1},
        {INF, INF, INF, 0}}
    floyd(g)


if __name__ =='__main__':
    main()