'''
Bell(n) = Sig k=1~n S(n, k)
S(n+1, k) = k*S(n,k) + S(n, k-1)
S(n+1, k) means n+1 elements in to k partition

Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }. 
'''

def simple_Partition(n):
    if n <=1:
        return 1
    
    arr = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        arr[i][i] = 1
        for j in range(1,i):
            arr[i][j] = j*arr[i-1][j] + arr[i-1][j-1]
    
    answer = 0
    for i in range(n+1):
        answer += arr[n][i]
    print(answer)
    
'''
Bell Traingle
1
1 2
2 3 5
5 7 10 15
if j == 0 --> b[i][j] = b[i-1][j-1]
else b[i][j] = b[i-1][j-1] + b[i][j-1]

'''
def DP(n):
    
    dp = [0 for _ in range(n)]
    dp[0] = 1

    for i in range(1, n):
        prev = dp[0]
        dp[0] = dp[i-1]
        for j in range(1,i+1):
            tmp = dp[j]
            dp[j] = prev + dp[j-1]
            prev = tmp
    print(dp[n-1])


def main():
    DP(5)
    
if __name__ == '__main__':
    main()
