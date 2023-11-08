from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        maxf = res = 0
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
            maxf = max(maxf, count[s[i]])
            if res - maxf < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res

        # maxf = ans = j = 0
        # n = len(s)
        # count = defaultdict(int)
        # for i in range(n):
        #     count[s[i]] += 1
        #     maxf = max(maxf, count[s[i]])
        #     if i - j + 1 - maxf > k:
        #         count[s[j]] -= 1
        #         j += 1
        #     ans = max(ans, i-j + 1)
        # return ans