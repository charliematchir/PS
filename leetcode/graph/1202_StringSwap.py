from collections import defaultdict
class Union:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        n = len(s)
        uf, g, res = Union(n), defaultdict(list), []
        for x, y in pairs:
            uf.union(x, y) if x < y else uf.union(y,x)
        for i in range(n):
            g[uf.find(i)].append(s[i])
        for li in g.values():
            li.sort(reverse=True)
        for i in range(n):
            res.append(g[uf.find(i)].pop())

        return "".join(res)

        # for i in range(n):
        #     g[uf.find(i)].append(i)
        # for li in g.values():
        #     chars = [s[i] for i in li]
        #     chars.sort()
        #     for i, c in zip(li, chars):
        #         res[i] = c
        #
        # return ''.join(res)


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        graph = defaultdict(list)
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)

        connected = self.dfs(graph)
        chars = []
        for c in connected:
            group = sorted(s[i] for i in c)
            chars.append(group)
        ans = list(s)
        for i in range(len(connected)):
            for j in range(len(connected[i])):
                idx = connected[i][j]
                char = chars[i][j]
                ans[idx] = char
        return ''.join(ans)

    def dfs(self, graph):
        connected = []
        visited = set()
        for idx in graph:
            if idx in visited:
                continue
            stack = [idx]
            group = []
            while stack:
                root = stack.pop()
                if root in visited:
                    continue
                group.append(root)
                visited.add(root)
                for nei in graph[root]:
                    stack.append(nei)
            connected.append(sorted(group))
        return connected