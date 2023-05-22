def Rec_bino(n,k):
    if k > n:
        return 0
    if n == k or k ==0:
        return 1
    
    else:
        return Rec_bino(n-1,k-1) + Rec_bino(n-1,k)


def DP_bino(n, k):
    if k>n:
        print("error")
        return
    elif k == 0 or n == k:
        print(1)
        return
    
    dp = [ [0]*(k+1) for _ in range(n+1)]

    for j in range(n+1):
        for i in range(min(j,k)+1):
            if i == 0 or j == i:
                dp[j][i] = 1
            else:
                dp[j][i] = dp[j-1][i-1] + dp[j-1][i]
    
    print(dp[n][k])

def Optimized_DP_bino(n, k):
    dp = [0 for i in range(k+1)]
    dp[0] = 1

    for i in range(n+1):
        j = min(i, k)

        while j > 0:
            dp[j] = dp[j] + dp[j-1]
            j-=1

        print(dp)
    



def main():
    Optimized_DP_bino(5,2)

if __name__ == '__main__':
    main()

