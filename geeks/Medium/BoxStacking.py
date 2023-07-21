def boxStack(height, width, length, n):
    rot = []

    for i in range(n):
        a = height[i]
        b = width[i]
        c = length[i]

        rot.append([a, min(b, c), max(b, c)])
        rot.append([b, min(a, c), max(a, c)])
        rot.append([c, min(a, b), max(a, b)])

    rot.sort(key=lambda x: x[1]*x[2], reverse=True)
    print(rot)
    n *= 3
    dp = [0] * n

    for i in range(n):
        dp[i] = rot[i][0]

    for i in range(1, n):
        for j in range(0, i):
            if rot[i][1] < rot[j][1] and rot[i][2] < rot[j][2]:
                dp[i] = max(dp[i], dp[j] + rot[i][0])

    print(max(dp))

def main():
    boxStack([4, 1, 4, 10], [6, 2, 5, 12], [7, 3, 6, 32], 4)


if __name__ == '__main__':
    main()