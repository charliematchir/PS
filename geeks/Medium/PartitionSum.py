
def psumSet(nums):
    N = len(nums)
    value = sum(nums)
    if value % 2 != 0:
        return False

    target = value // 2

    if target in nums:
        return True

    s = {nums[0], 0}
    temp = set()
    for i in range(1, N):
        for v in s:
            if v + nums[i] <= target:
                temp.add(v + nums[i])
        if target in temp:
            return True
        s.update(temp)
        temp.clear()

    return False


def psumRec(N, arr, target):

    if target == 0:
        return True

    if target < 0 or N==0:
        return False

    return psumRec(N-1, arr, target-arr[N-1]) or psumRec(N-1, arr, target)


def psumDP(N, arr):
    val = sum(arr)
    if val % 2 != 0:
        return False
    target = val // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[-1]

def main():
    print(psumSet(5, [2, 4, 11, 10, 5]))


if __name__ == '__main__':
    main()