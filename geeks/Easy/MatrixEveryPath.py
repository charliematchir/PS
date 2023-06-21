
def MatrixPath(n, m):
    arr = [[1]*m for _ in range(n)]

    arr[0][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    print(arr[n-1][m-1])


def spaceOpt(n, m):
    arr = [1] * m

    for i in range(1, n):
        for j in range(1, m):
            arr[j] = arr[j]+arr[j-1]
    print(arr[-1])
def main():
    MatrixPath(6, 7)
    spaceOpt(6, 7)
if __name__ == '__main__':
    main()
