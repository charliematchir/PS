'''
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
'''

def rec_subsum(nums, idx, target):
    if tagert == 0:
        return True

    if target > 0 and idx == -1:
        return False

    if nums[idx] > target:
        return rec_subsum(nums, idx-1, target)
    
    return rec_subsum(nums, idx-1, target) or rec_subsum(nums, idx-1, target-nums[idx])


table = [ [-1] * 10  for _ in range(10)]
def topdown_subSum(nums, idx, target):

    if target == 0:
        return 1

    if idx <= -1:
        return 0

    if table[idx][target] != -1:
        return table[idx][target]

    if nums[idx] > target:
        table[idx][target] = topdown_subSum(nums, idx-1, target)
        return table[idx][target]
    else:
        table[idx][target] = topdown_subSum(nums, idx-1, target)
        return table[idx][target] or topdown_subSum(nums, idx-1, target-nums[idx])


def bottomup_subSum(nums, target):
    
    n = len(nums)
    dp = [[False]*(target+1) for _ in range(n+1)]
    dp[0][0] = True
    for j in range(1,n+1):
        dp[j][0] = True
        for i in range(1, target+1):
            if i >= nums[j-1]:
                dp[j][i] = dp[j-1][i] or dp[j][i-nums[j-1]]
            else:
                dp[j][i] = dp[j-1][i]

    return dp[n][target]
    


def main():
    nums = [3,34, 4, 12, 5,2]
    n = len(nums)
    target = 9
    '''
    if rec_subsum(nums, len(nums)-1, target):
        print("True")
    else:
        print("False")
    
    if topdown_subSum(nums, n-1, target):
        print("yes")
    else:
        print("No")
    '''
    if bottomup_subSum(nums, target):
        print("Yes")
if __name__ =='__main__':
    main()


