def LCSubstr2D(x, y):
    n, m = len(x), len(y)
    dp = [[0]*(m+1) for _ in range(n+1)]
    length = 0 
    end_row = 0
    
    for i in range(1, n+1):
        for j in range(1,m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > length:
                    length = dp[i][j]
                    end_row = i-1

    ans = x[end_row-length+1:end_row+1]
    print(ans)

# 2D LCS 도 문자 비교시 사용하는 건 바로 전 Row 일 뿐
# 2개의 Row 만 유지하면서 번갈아 가는것으로 space optimize
def LCSubstr1D(x, y):
    m, n = len(x), len(y)
    dp = [[0]*(n+1) for _ in range(2)]
    length = 0
    curr = 0
    end_idx = 0
    
    for i in range(1, m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                dp[curr][j] = dp[1-curr][j-1] + 1
                if dp[curr][j] > length:
                    length = dp[curr][j]
                    end_idx = i-1
        curr = 1 - curr
    ans = x[end_idx - length + 1: end_idx + 1]
    print(ans)

def lcs_best (str1, str2):
    m = len(str1)
    n = len(str2)

    # Initialize variables to keep track of the maximum length and its ending index
    max_length = 0
    ending_index = 0

    # Initialize the previous row and previous diagonal elements
    prev_row = [0] * (n + 1)
    prev_diag = 0

    # Update the length matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            current_length = 0

            if str1[i - 1] == str2[j - 1]:
                current_length = prev_diag + 1
                if current_length > max_length:
                    max_length = current_length
                    ending_index = i - 1
            # Update the previous diagonal element
            prev_diag = prev_row[j]
            # Update the previous row
            prev_row[j] = current_length

    # Retrieve the longest common substring
    longest_substring = str1[ending_index - max_length + 1 : ending_index + 1]

    return longest_substring


def main():
    str1 = "abcdxyz"
    str2 = "xyzabcd"

    X = "GeeksforGeeksQ";
    Y = "GeeksQuiz";
    print(lcs(X,Y))
    LCSubstr2D(str1, str2)  
    LCSubstr1D(str1, str2)
if __name__ == '__main__':
    main()
