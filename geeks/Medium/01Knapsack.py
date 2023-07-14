
def main():
    # N itmes and Bag Cap
    # N, Cap = 3, 4
    # profit = [1, 2, 3]
    # weight = [4, 5, 1]

    N, Cap = 3, 50
    profit = [61, 100, 120]
    weight = [15, 20, 30]
    #
    # N, Cap = 4, 60
    # profit = [40, 100, 50, 60]
    # weight = [20, 10, 40, 30]

    # N = 2
    # Cap = 4
    # profit = [6, 18]
    # weight = [2, 3]

    # unbounded_knapSack(profit, weight, Cap, N)
    unbounded_knapSack(Cap, weight, profit, N)


def knapsack_rec(profit, weight, cap, n):
    if n == 0 or cap == 0:
        return 0
    if weight[n-1] > cap:
        return knapsack_rec(cap, n-1, profit, weight)
    else:
        return max(profit[n-1] + knapsack_rec(cap-weight[n-1], n-1, profit, weight),
                   knapsack_rec(cap, n-1, profit, weight))

def knapsack_dp(profit, weight, cap, n):
    dp= [[0]*(cap+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(cap+1):
            if i == 0 or w == 0:
                continue
            if w >= weight[i-1]:
                # w에서 현재 item 선택 했을때 vs 선택 안했을 때
                dp[i][w] = max(dp[i-1][w-weight[i-1]]+profit[i-1], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]


def knapSack(W, wt, val, n):
    dp = [0] * (W + 1)

    for i in range(1, n + 1):
        for w in range(W, 0, -1):
            if w >= wt[i - 1]:
                dp[w] = max(dp[w - wt[i - 1]] + val[i - 1], dp[w])

    return dp[-1]


def knapsack_print(profit, weight, cap, n):
    dp= [[0]*(cap+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(cap+1):
            if i == 0 or w == 0:
                continue
            if w >= weight[i-1]:
                # w에서 현재 item 선택 했을때 vs 선택 안했을 때
                dp[i][w] = max(dp[i-1][w-weight[i-1]]+profit[i-1], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    j = cap
    answer = []
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            answer.append(weight[i-1])
            j -= weight[i-1]

    print(dp[-1][-1])
    print(answer)

def unbounded_knapSack(W, wt, val, n):
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(1, W+1):
            if w >= wt[i]:
                dp[w] = max(dp[w - wt[i]] + val[i], dp[w])
    print(dp)

    dp = [0] * (W + 1)
    for w in range(1, W + 1):
        for i in range(n):
            if w >= wt[i]:
                dp[w] = max(dp[w - wt[i]] + val[i], dp[w])
    print(dp)



if __name__ == '__main__':
    main()
