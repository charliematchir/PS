def TSP(graph):

    # dp[i][j] 에서 i 에서 출발점, j 는 현재 방문 상황을 bit로 나타낸 것이고, dp[i][j]는 남은 위치들의 방문 거리 최소값이다.
    n = len(graph)
    dp = [[float('inf')] * (1 << n) for _ in range(n)]

    def helper(curr_node, visited):
        if visited == (1 << n) - 1:
            return graph[curr_node][0]

        if dp[curr_node][visited] != float('inf'):
            return dp[curr_node][visited]

        min_dist = float('inf')

        for i in range(1, n):
            if visited & (1 << i) == 0:
                new_visited = visited | (1 << i)
                min_dist = min(min_dist, graph[curr_node][i] + helper(i, new_visited))
        dp[curr_node][visited] = min_dist
        return dp[curr_node][visited]

    return helper(0, 1)



def main():
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print(TSP(graph))


if __name__ == '__main__':
    main()