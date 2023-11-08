def wb(s, wordDict):

    # n = len(s)
    # dp = [False] * (n + 1)
    # dp[0] = True
    # for i in range(n):
    #     if dp[i] == False:
    #         continue
    #     for w in wordDict:
    #         if len(w) <= n - i:
    #             if s[i: i + len(w)] == w:
    #                 dp[i + len(w)] = True
    # return dp[n]


    # Break Point 가 i에서 시작 하는경우는 early break 가 가능
    n = len(s)
    dp = [False] * (n + 1)
    dp[n] = True
    for i in range(n-1, -1, -1):
        for w in wordDict:
            if i + len(w) <= n and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]


def main():
    wd = ["cats","dog","sand","and","cat"]
    s = "catsandog"
    print(wb(s, wd))


if __name__=='__main__':
    main()