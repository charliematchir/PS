class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)
        if k == n:
            return "0"

        stk = []

        idx = 0
        for v in num:
            while k > 0 and stk and (stk[-1] > v):
                stk.pop()
                k -= 1

            if v != '0' or stk:
                stk.append(v)

        # while k > 0 and stk:
        #     stk.pop()
        #     k-=1

        if k:
            stk = stk[0:-k]

        return ''.join(stk) or '0'

