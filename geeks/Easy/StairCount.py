def StairWays(N):
    if N < 2:
        return N

    dp = [0]*N
    dp[0] = 1
    dp[1] = 2
    dp[2] = 3

    for i in range(3, N):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[-1]


def main():
    N = 10
    StairWays(N)

if __name__ == '__main__':
    main()
