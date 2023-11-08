from collections import defaultdict


class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """

        graph = defaultdict(list)

        for st, ed in edges:
            graph[st].append(ed)
            graph[ed].append(st)

        visited = set([bob])
        path = [bob]

        def bobdfs(start):
            if start == 0:
                n = len(path)
                if n % 2 != 0:
                    amount[path[n // 2]] /= 2
                    for i in range(n // 2):
                        amount[path[i]] = 0
                else:
                    for i in range(n // 2):
                        amount[path[i]] = 0
                return

            if 0 in visited:
                return

            for nei in graph[start]:
                if nei not in visited:
                    visited.add(nei)
                    path.append(nei)
                    bobdfs(nei)
                    visited.discard(nei)
                    path.pop()

        bobdfs(bob)
        path = [0]
        visited = set([0])
        answer = [-float('inf')]

        def dfs(start, value):
            flag = 1

            for nei in graph[start]:
                if nei not in visited:
                    flag = 0
                    visited.add(nei)
                    path.append(nei)
                    dfs(nei, value + amount[nei])
                    visited.discard(nei)
                    path.pop()

            if flag == 1:
                answer[0] = max(answer[0], value)

        dfs(0, amount[0])
        return answer[0]
