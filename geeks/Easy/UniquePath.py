def uniquePath(grid):
    n, m = len(grid), len(grid[0])

    path = [[0]*n for _ in range(m)]

    for j in range(n):
        if path[j][0] == 1:
            break
        else:
            path[j][0] = 1
    for i in range(m):
        if path[0][i] == 1:
            break
        else:
            path[0][i] = 1

    for j in range(1, n):
        for i in range(1, m):
            if grid[j][i] == 0:
                path[j][i] = path[j - 1][i] + path[j][i - 1]

    print(path[-1][-1])
def main():
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    uniquePath(grid)

if __name__ == '__main__':
    main()
