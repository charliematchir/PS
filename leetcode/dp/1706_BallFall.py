class Solution(object):
    def findBall(self, grid):

        row, col = len(grid), len(grid[0])
        answer = [-1] * col

        for i in range(col):
            r, c = 0, i
            while r < row:
                if grid[r][c] == 1:
                    if c == col - 1:
                        break
                    elif grid[r][c + 1] == -1:
                        break
                    else:
                        c += 1
                elif grid[r][c] == -1:
                    if c == 0:
                        break
                    elif grid[r][c - 1] == 1:
                        break
                    else:
                        c -= 1
                r += 1

                if r == row:
                    answer[i] = c

        return answer