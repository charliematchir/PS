
INF = 987654321

def eggDrop(N, K):
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        dp[i][1] = 1
    for j in range(1, K+1):
        dp[1][j] = j

    for i in range(2, N+1):
        for j in range(2, K+1):
            dp[i][j] = INF
            for x in range(1, j+1):
                v = max(dp[i][j-x], dp[i-1][x-1]) + 1
                dp[i][j] = min(dp[i][j], v)
    print(dp[-1][-1])

def eggDrop_opt(n, k):
    dp = [0 for i in range(n+1)]
    m = 0
    while dp[n] < k:
        m += 1
        for x in range(n, 0, -1):
            dp[x] += 1 + dp[x - 1]
    print(m)


def main():
    eggDrop(2, 36)

if __name__ == '__main__':
    main()