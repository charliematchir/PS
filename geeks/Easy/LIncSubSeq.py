def LIS(li):
    n = len(li)
    dp = [1] *n
    for i in range(1,n):
        for j in range(i):
            if li[i] > li[j] and dp[j]+1 > dp[i]:
                dp[i] = dp[j] + 1
    
    answer = 0
    for v in dp:
        if v > answer:
            answer = v
    print(answer)

# O(N^2)
# LIS is Same as LCS between sorted li and li



def LCS_like(li):
    n = len(li)
    sorted_li = sorted(li)
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1,n+1):
            if li[i-1] == sorted_li[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[-1][-1])


#O(N*logN) // Patience Sorting
# But not exat oreder
def Fast_LCS_like(li):
    n = len(li)
    dp = [0]* n
    
    size = 0
    for v in li:
        left, right = 0, size

        while left < right:
            mid = (left+right)//2
            if li[mid] < v:
                left = mid + 1
            else:
                right = mid

        tails[left] = num
        size = max(size, left + 1)

    print(size)


def lis_exact_order(nums):
    n = len(nums)
    lengths = [1] * n  # Initialize lengths array
    previous = [-1] * n  # Initialize previous array

    # Find the length of the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lengths[i] <= lengths[j]:
                lengths[i] = lengths[j] + 1
                previous[i] = j

    max_length = max(lengths)
    end_index = lengths.index(max_length)  # Index of the last element in the LIS

    # Retrieve the exact order of the LIS
    lis_order = []
    while end_index != -1:
        lis_order.append(nums[end_index])
        end_index = previous[end_index]

    lis_order.reverse()  # Reverse the order to get the actual LIS

    return lis_order


# Finding all possible combinations
# O(k*N^2)
def lis_with_numbers(nums):
    n = len(nums)
    lengths = [1] * n  # Initialize lengths array

    # Find the length of the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lengths[i] <= lengths[j]:
                lengths[i] = lengths[j] + 1

    max_length = max(lengths)  # Maximum length of the LIS

    # Retrieve all the longest increasing subsequences
    subsequences = []
    current_subsequence = []

    def backtrack(index, length):
        nonlocal current_subsequence

        if length == 0:
            subsequences.append(current_subsequence[:])
            return

        for i in range(index, -1, -1):
            if lengths[i] == length and (length == max_length or nums[i] < current_subsequence[-1]):
                current_subsequence.append(nums[i])
                backtrack(i - 1, length - 1)
                current_subsequence.pop()

    for i in range(n - 1, -1, -1):
        if lengths[i] == max_length:
            current_subsequence.append(nums[i])
            backtrack(i - 1, max_length - 1)
            current_subsequence.pop()

    return max_length, subsequences


# For finding number of comb of maximum length

def count_lis_combinations(nums):
    n = len(nums)
    lengths = [1] * n  # Initialize lengths array
    counts = [1] * n  # Initialize counts array

    # Find the length of the longest increasing subsequence and counts
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lengths[i] <= lengths[j]:
                lengths[i] = lengths[j] + 1
                counts[i] = counts[j]
            elif nums[i] > nums[j] and lengths[i] == lengths[j] + 1:
                counts[i] += counts[j]
    max_length = max(lengths)  # Maximum length of the LIS

    # Calculate the total count of combinations for the maximum length
    total_count = sum(count for length, count in zip(lengths, counts) if length == max_length)

    return total_count



def main():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    li = [50, 3, 10, 7, 40, 80]
    
    #LIS(arr)
    seq = [10,9,2,5,3,7,101,18]
    n, l = lis_with_numbers(seq)
    v = count_lis_combinations(seq)
    #print(n)
    print(l)
    print(v)

if __name__== '__main__':
	main()

