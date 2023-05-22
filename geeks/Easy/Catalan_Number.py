'''

Cn = (2n)! / ( (n+1)! n! )
C0 = 1 and Cn+1 = Sig i=0~n ( Ci * Cn-i )

'''

def Recursive_catalan(n):
    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += catalan(i)*catalan(n-i-1)
    
    return res


def DP_catalan(n):
    
    if n==0 or n == 1:
        return 1
    dp = [0]* (n+1)

    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[n-j-1]
    
    return dp[n]

    
