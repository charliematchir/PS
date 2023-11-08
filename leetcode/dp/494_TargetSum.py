class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total = sum(nums)

        if total < abs(target) or (total + target) % 2 != 0:
            return 0
        # Calculate the target sum for subset sum problem
        W = (total + target) // 2
        dp = [0] * (W + 1)
        dp[0] = 1
        for num in nums:
            for j in range(W, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[W]

        # n = len(nums)
        # value = sum(nums)
        # dp = defaultdict(int)
        # dp[value] = 1

        # for val in nums:
        #     for k, v in dp.items():
        #         if k < target:
        #             continue
        #         dp[k-2*val] += v

        # return dp[target]