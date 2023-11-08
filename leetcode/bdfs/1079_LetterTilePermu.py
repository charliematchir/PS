# class Solution(object):
#     res = 0
#     def numTilePossibilities(self, tiles):
#         """
#         :type tiles: str
#         :rtype: int
#         """
#         freq = collections.defaultdict(int)
#         for c in tiles:
#             freq[c] += 1
#
#
#         def dfs(st):
#             for c in freq:
#                 if freq[c] > 0:
#                     self.res += 1
#                     freq[c] -= 1
#                     dfs(st+c)
#                     freq[c] += 1
#         dfs('')
#         return self.res


class Solution(object):
    def numTilePossibilities(self, tiles):
        letter_count = {}
        for letter in tiles:
            letter_count[letter] = letter_count.get(letter, 0) + 1

        memo = {}

        print(letter_count.items())

        def backtrack(counts):
            counts_tuple = tuple(counts.items())
            total = 0
            if counts_tuple not in memo:
                for letter, count in counts.items():
                    if count == 0:
                        continue
                    # Include the current letter in the sequence
                    total += 1
                    counts[letter] -= 1
                    total += backtrack(counts)
                    counts[letter] += 1
                memo[counts_tuple] = total
            return memo[counts_tuple]

        return backtrack(letter_count)




