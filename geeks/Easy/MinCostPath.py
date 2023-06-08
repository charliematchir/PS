
def minCost(arr):
    row, col = len(arr), len(arr[0])
    dp = [rows for rows in arr]
    
    for i in range(1, row):
        dp[i][0] += dp[i-1][0]

    for i in range(1, col):
        dp[0][i] += dp[0][i-1]

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] += min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    print(dp)
    

def main():
    arr = [ [1,2,3], [4,8,2], [1,5,3]]
    minCost(arr)

if __name__ == '__main__':
    main()
