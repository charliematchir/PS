class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        def countZero(yp, xp):
            ans = 1
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                y, x = yp + dy, xp + dx
                if grid[y][x] == 0:
                    if (y == 0 or y == n - 1 or x == 0 or x == m - 1):
                        ans = 0
                    else:
                        grid[y][x] = 2
                        ans *= countZero(y, x)
            return ans

        answer = 0

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if grid[i][j] == 0:
                    answer += countZero(i, j)
        return answer



###  BFS ####
# class Solution(object):
#     def closedIsland(self, grid):
#         n = len(grid)
#         if n < 1:
#             return 0
#         m = len(grid[0])

#         def island(grid, row_index, col_index):
#             bfs = []
#             grid[row_index][col_index]=2
#             bfs.append([row_index, col_index])
#             index = 0
#             flag = False
#             while index < len(bfs):
#                 r, c = bfs[index]
#                 for dy, dx in [(1,0), (0, 1), (-1, 0), (0,-1)]:
#                     y, x = r+dy, c+dx
#                     if grid[y][x] == 0:
#                         if y == 0 or y == n-1 or x == 0 or x == m-1:
#                             flag = True
#                             continue
#                         else:
#                             grid[y][x] = 2
#                             bfs.append([y, x])
#                 index += 1
#             return False if flag else True

#         islands = 0
#         for row_index in range(1, n-1):
#             for col_index in range(1,m-1):
#                 if grid[row_index][col_index] == 0:
#                     if island(grid, row_index, col_index):
#                         islands += 1
#         return islands