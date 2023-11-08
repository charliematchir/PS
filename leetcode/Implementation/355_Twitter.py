from collections import defaultdict
from collections import deque
import itertools
import heapq
# heap[k] <= heap[2k+1] and <= heap[2k+2]
# heappush, heappop  O(logN)
# heapify O(N)
# heapq.merge 는 정렬된 iterable들을 단일 정렬시킨다.
# nlargest(n, iterable), nsmallest

class Twitter(object):
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

        # res = []
        # heap = []
        #
        # for usr in self.following[userId] | {userId}:
        #     if usr in self.tweets:
        #         tweets = self.tweets[usr]
        #         for x in tweets:
        #             heapq.heappush(heap, x)
        #
        # while len(res) < 10 and heap:
        #     res.append(heapq.heappop(heap)[1])
        #
        # return res

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)
