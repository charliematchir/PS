from collections import deque
'''  

class Solution:
    def minDistance(self, word1, word2):
        ################################################
        if word1 == word2:
            return 0
        
        memo = {}
        def dfs(idx1, idx2):
            if idx2 == m or idx1 == n:
                return n-idx1 + m-idx2
            
            # memoization 으로 idx1, idx2 이미 memo에 있으면 return
            if (idx1,idx2) in memo:
                return momo[(idx1,idx2)]
            
            if word1[idx1] == word2[idx2]:
                ans = dfs(idx1+1, idx2+1)
            else:
                ans = 1 + min(dfs(idx1+1, idx2+1), dfs(idx1+1, idx2),dfs(idx1,idx2+1))
            momo[(idx1,idx2)] = ans
            return memo[(idx1,idx2)]
        return dfs(0, 0)
        ################################################
        
        ################################################
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])
        return min(insert, replace, delete)
        ################################################
'''



#### DP ####
class Solution(object):
    def minDistance(self, word1, word2):
        ################################################
        if word1 == word2:
            return 0

        n, m = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word2[i-1] == word1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        ################################################
        if word1 == word2:
            return 0
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        w1 = list(word1)
        w2 = list(word2)
        num = 0
        queue = deque([(0,0)])

        visited = set()
        while len(queue) > 0:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
                    i += 1
                    j += 1
                if i == len(w1) and j == len(w2):
                    return num
                queue.append((i, j + 1))
                queue.append((i + 1, j + 1))
                queue.append((i + 1, j))
            num += 1
        ################################################


