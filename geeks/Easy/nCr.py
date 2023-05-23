mod = 10**9+7

'''
C(n, r)%p = [ C(n-1, r-1)%p + C(n-1, r)%p ] % p
time Complexity= O(nr)
space Complexity = O(r)

'''

def nCr(self, n, r):
    dp = [0 for _ in range(r+1)]
    dp[0] = 1
    # Compute next row of pascal triangle using previous row
    for i in range(1, n+1):
        j = min(i, r)
        while (j > 0):
            dp[j] = (dp[j] + dp[j-1]) % mod
            j -= 1

    return dp[r]


