class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # h 는 팔지 않았을때 이익 최대 값
        # r은 팔았을때 이익 최대값
        # h1, h2 = -float('inf'), -float('inf')
        # r1, r2 = 0, 0
        # for v in prices:
        #     r2 = max(r2, h2 + v)
        #     h2 = max(h2, r1 - v)
        #     r1 = max(r1, h1 + v)
        #     h1 = max(h1, -v)
        # return r2

        # buy1, buy2 = float('inf'), float('inf')
        # sell1, sell2 = 0, 0
        # for v in prices:
        #     buy1 = min(buy1, v)
        #     sell1 = max(sell1, v-buy1)
        #     buy2 = min(buy2, v-sell1)
        #     sell2 = max(sell2, v-buy2)
        # return sell2

        # lowest1, lowest2 = float('inf'), float('inf')
        # maxP1, maxP2 = 0, 0
        # for v in prices:
        #     maxP2 = max(maxP2, v - lowest2)
        #     lowest2 = min(lowest2, v-maxP1)
        #     maxP1 = max(maxP1, v - lowest1)
        #     lowest1 = min(lowest1, v)
        # return maxP2
