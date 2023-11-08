

def LPS_rec(s, i, j):
    if i == j:
        return 1
    if s[i] == s[j]:
        if i + 1 == j:
            return 2
        return LPS_rec(s, i+1, j-1) + 2
    return max(LPS_rec(s, i+1, j), LPS_rec(s, i, j-1))


## LCS on s and s_rev
def LPS_dp(s):
    s_rev = s[::-1]
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[j-1] == s_rev[i-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[-1][-1])

# dp[i][j] represents the length of the longest palindromic subsequence in the substring s[i:j+1]
# dp[i][i] 는 s[i]하나를 뜻해서 1로 초기화
# state transition
# if s[i] == s[j] => dp[i][j] = dp[i+1][j-1] +2  else => dp[i][j] = max(dp[i+1][j], dp[i][j-1])
def LPS_DP_opt(s):
    n = len(s)
    # ####### Smaller to Larger String ########
    # dp = [[0] * n for _ in range(n)]
    # for i in range(n):
    #     dp[i][i] = 1
    #
    # for substr_len in range(2, n+1):
    #     for i in range(n-substr_len+1):
    #         #
    #         j = i + substr_len - 1
    #         if s[i] == s[j]:
    #             if substr_len == 2:
    #                 dp[i][j] = 2
    #             else:
    #                 dp[i][j] = dp[i+1][j-1] + 2
    #         else:
    #             dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    # print(dp[0][n - 1])
    # #####################################
    #
    #
    # ########## Two Pointer ##############
    # dp = [[0] * n for _ in range(n)]
    # for i in range(n-1, -1, -1):
    #     dp[i][i] = 1
    #     for j in range(i+1, n):
    #         if s[i] == s[j]:
    #             dp[i][j] = dp[i+1][j-1] + 2
    #         else:
    #             dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    # print(dp[0])
    # ######################################


    ########## Space Opt #################
    dp = [1] * n
    for i in range(n-1, -1, -1):
        prev = 0
        for j in range(i+1, n):
            # 현재의 temp는 다음 j+1 에서의 prev로 쓰이는거고
            # 현재 값이 j+1에서 dp[i+1][j-1] 값 역할.
            temp = dp[j]
            if s[i] == s[j]:
                dp[j] = prev + 2
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev = temp
    print(dp)
    ######################################

def main():
    s = "BBABCBCAB"
    # LPS_dp(s)
    s1 = "bbbab"
    LPS_DP_opt(s)
    LPS_DP_opt(s1)

if __name__=='__main__':
    main()