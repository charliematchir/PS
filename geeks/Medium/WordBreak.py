def wb(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(n):
        if dp[i] == False:
            continue

        for w in wordDict:
            if len(w) <= n - i:
                if s[i: i + len(w)] == w:
                    dp[i + len(w)] = True
    return dp[n]

    for i in range(n):
        if dp[n]:
            return dp[n]
        if dp[i]:
            for j in range(i, n):
                if s[i:j+1] in wordDict:
                    dp[j+1] = True
    return dp[n]


def main():
    wd = ["cats","dog","sand","and","cat"]
    s = "catsandog"
    print(wb(s, wd))


if __name__=='__main__':
    main()