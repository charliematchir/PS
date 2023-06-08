
def longestSubsequence(self, N, A):
        # code here

        dp = [1] * N;
        ans = 1
        for i in range(1, N):
            for j in range(i):
                if abs(A[i] -A[j]) == 1 and dp[j]>=dp[i]:
                    dp[i] = dp[j] + 1
            ans = max(dp[i], ans)

        return ans


## leetcode 128 is similar
def longestSubsequence(A, N):
    L = [1]*N
    hm = {}
    for i in range(1,N):
        if abs(A[i]-A[i-1]) == 1:
            L[i] = 1 + L[i-1]
        elif hm.get(A[i]+1,0) or hm.get(A[i]-1,0):
            L[i] = 1+max(hm.get(A[i]+1,0), hm.get(A[i]-1,0))
        hm[A[i]] = L[i] # 빈 dict에서 시작해서 추가하거나 업데이트 하는것
    return max(L)


def main():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    li = [50, 3, 10, 7, 40, 80]
    seq = [10,9,2,5,3,7,101,18]

if __name__== '__main__':
	main()

