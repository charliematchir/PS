
def MaxSizeSquare(arr):
    Row, Col = len(arr), len(arr[0])
    size = 1
    yp, xp = 0, 0
    for i in range(Row):
        for j in range(Col):
            if arr[i][j] == 1:
                cnt, flag = 1, 0
                while (j+cnt<Col and i+cnt<Row and flag != 1):
                    for x, y in zip(range(j, j+cnt+1), range(i, i+cnt+1)):
                        if  arr[i+cnt][x] != 1 or arr[y][j+cnt] != 1:
                            flag = 1
                            break
                    if flag:
                        break
                    cnt+=1
                value = cnt 
                if value > size:
                    size = value
                    yp, xp = i, j
    
    print(size)
    print(yp, xp)
            

def dpSize(arr):
    dp = [rows for rows in arr]
    Row, Col = len(arr), len(arr[0])
    answer,yp, xp = 0, 0, 0
    for i in range(1, Row):
        for j in range(1, Col):
            if dp[i][j] != 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
            
            if answer <dp[i][j]:
                answer = dp[i][j]
                yp,xp = i, j
    print(dp)
    print(answer, yp, xp)

def main():
    M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]

    
    #MaxSizeSquare(M)
    dpSize(M)
if __name__ == '__main__':
    main()
