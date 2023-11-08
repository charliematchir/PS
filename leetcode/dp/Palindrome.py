def Longest_Palindrome_SubString(s):
    n = len(s)

    dp = [[False]*(n) for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    max_l = 0
    st, ed = 0, 0
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                if j-i <= 1 or dp[i+1][j-1]:
                    dp[i][j] = True
                    # for counting Palindrom SubString,
                    # Just answer +=1 at here and comment below
                    if j-i > max_l:
                        ed, st = j, i
                        max_l = j-i
    print(s[st:ed+1])


def Palindrome_SubSeqRec(s):
    n = len(s)
    def rec(i , j):
        if j == i:
            return 1
        if s[i] == s[j] and j-i == 1:
            return 2

        if s[i] == s[j]:
            return 2 + rec(i+1, j-1)
        else:
            return max(rec(i+1, j), rec(i, j-1))


def Longest_Palindrome_SubSeq(s):
    n = len(s)

    # dp = [[0] * n for _ in range(n)]
    # for i in range(n-1, -1, -1):
    #     dp[i][i] = 1
    #     for j in range(i+1, n):
    #         if s[i-1] == s[j-1]:
    #             dp[i][j] = dp[i+1][j-1] + 2
    #         else:
    #             dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    # Space Optimize
    dp = [1] * n
    for i in range(n-1, -1, -1):
        prev = 0
        for j in range(i+1, n):
            temp = dp[j]
            if s[i-1] == s[j-1]:
                dp[j] = prev + 2
            else:
                dp[j] = max(dp[j], dp[j-1])
            prev = temp


def Palindrome_Partition(s):
    n = len(s)
    answer = []
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = True
        for j in range(i + 1, n):
            if s[i] == s[j]:
                if j - i <= 1 or dp[i + 1][j - 1]:
                    dp[i][j] = True

    def backtrack(temp, idx_j):
        if idx_j == n:
            answer.append(temp)
            return

        for x in range(idx_j, n):
            if dp[idx_j][x]:
                backtrack(temp+[s[idx_j:x+1]], x+1)

    backtrack([], 0)
    print(answer)



def main():
    # BABCBAB
    # s = "BBABCBCAB"
    # s = "aab"
    # s = "aabaa"
    s = "aacecaaa"
    s= "aabba"
    Longest_Palindrome_SubString(s)


if __name__ == '__main__':
    main()