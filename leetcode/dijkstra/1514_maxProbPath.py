class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        graph = collections.defaultdict(dict)

        for (src, dst), prob in zip(edges, succProb):
            graph[src][dst] = prob
            graph[dst][src] = prob

        prob = [-1.0] * n
        pq = [(-1.0, start)]

        while pq:
            p, node = heapq.heappop(pq)
            if -p < prob[node]:
                continue
            if node == end:
                break

            for nei, pb in graph[node].items():
                if prob[nei] < (-p) * pb:
                    prob[nei] = (-p) * pb
                    heapq.heappush(pq, (-prob[nei], nei))

        return prob[end] if prob[end] != -1.0 else 0.0