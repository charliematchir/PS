class Solution(object):
    def wordBreak(self, s, wordDict):
        n, answer = len(s), []
        maxl = max(len(w) for w in wordDict)

        def wbrec(ans, st):
            m = len(st)
            if m == 0:
                answer.append(" ".join(ans))
                return
            r = max(maxl, m)
            for i in range(r):
                for w in wordDict:
                    if i + 1 == len(w) and st[:i + 1] == w:
                        ans.append(w)
                        wbrec(ans[:], st[i + 1:])
                        ans.pop()
            return

        wbrec([], s)
        return answer


        # memo
        '''
        word_set = set(wordDict)
        memo = {}

        def findSentence(s):
            if s in memo:
                return memo[s]
            if not s:
                return []
            res = []
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    right_sents = findSentence(s[i:])
                    if right_sents:
                        for right_sent in right_sents:
                            res.append(s[:i] + " " + right_sent)

                    elif not s[i:]:
                        res.append(s[:i])

            memo[s] = res
            return res
        '''

        # for loop 안에서 recursive 하게 append 하는 방식
        '''
         
        dp = {}
        def go(cur):
            if cur >= len(s):
                return [""]
            if cur in dp:
                return dp[cur]
            ret = []
            for word in wordDict:
                if word == s[cur:cur + len(word)]:
                    for p in go(cur + len(word)):
                        ret.append(word + " " + p)
            dp[cur] = ret
            return ret
        return [split[:len(split) - 1] for split in go(0)]
        '''