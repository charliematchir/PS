def LCS(str1, str2):
    n, m = len(str1), len(str2)
    dp = [ [0]*(n+1) for _ in range(m+1) ]
    
    for j in range(1,m+1):
        for i in range(1,n+1):
            if str2[j-1] == str1[i-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])
    print(dp[m][n])

def main():
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    LCS(s1, s2)

if __name__== '__main__':
	main()

