# assert n < m !
# without dup k !
def tower_rec(n, m):
    result =[]
    curr = []
    def rec(count, idx):
        if count == 0:
            result.append(curr[:])
            return

        for i in range(idx, m+1):
            curr.append(i)
            rec(count-1, idx+1)
            curr.pop()

    rec(n, 1)
    return len(result)
def tower_dp(n, m):
    dp = [[0] * m for _ in range(n)]

    for i in range(m):
        dp[0][i] = i+1

    for i in range(1, n):
        for j in range(i, m):
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp)


# 1 ~ m size tile
# can use k tiles of same size
# number of ways to build n height tower
def tileStack(n, m, k):

    if n > m*k:
        return 0
    if n == 1:
        return m
    if m == 1:
        return 1 if n <= k else 0

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, m+1):
        dp[1][i] = i

    for i in range(2, n+1):
        for j in range(1, m+1):
            for l in range(k+1):
                if l > i:
                    break
                elif l == i:
                    dp[i][j] += 1
                else:
                    dp[i][j] += dp[i-l][j-1]
    print(dp)


def main():
    tileStack(3, 3, 2)

if __name__ == '__main__':
    main()