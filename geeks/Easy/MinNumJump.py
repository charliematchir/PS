def minJump(arr):
    n = len(arr)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if arr[j]>= i-j:
                dp[i] = min(dp[j] + 1, dp[i])

    print(dp[-1])


# Greedy O(N)
def GreedyJump(arr):
    n = len(arr)
    max_reach = arr[0]
    step = arr[0]
    jumps = 0

    for i in range(1, n):
        if i == n-1:
            return jumps + 1
        max_reach = max(max_reach, i+arr[i])
        
        step -= 1
        if step ==0:
            if i >= max_reach:
                return -1
            step = max_reach - i
            jumps += 1
    
    return -1
        

def main():
    arr = [1, 3, 5, 6, 9, 2, 6, 7, 6, 8, 9]
    minJump(arr)
    print(GreedyJump(arr))
if __name__ == '__main__':
    main()
