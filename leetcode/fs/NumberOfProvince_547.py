class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        graph = {idx:[] for idx in range(n)}

        for j in range(n-1):
            for i, v in enumerate(isConnected[j][j+1:]):
                if v == 1:
                    graph[j].append(j+i+1)
                    graph[j+i+1].append(j)

        visited = set()

        def dfs(idx):
            visited.add(idx)
            for v in graph[idx]:
                if v not in visited:
                    dfs(v)
            return

        answer = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                for v in graph[i]:
                    dfs(v)
                answer +=1
        return answer
        
        
        ###### BFS ######
        # s = set()
        # n = len(isConnected)
        # st = []
        # count = 0
        # for i in range(n):
        #     if i in s:
        #         continue
        #     count+=1
        #     s.add(i)
        #     st.append(i)
        #     while st:
        #         el = st.pop()
        #         for adj_el in range(n):
        #             if isConnected[el][adj_el] and adj_el not in s:
        #                 s.add(adj_el)
        #                 st.append(adj_el)
        # return count 
