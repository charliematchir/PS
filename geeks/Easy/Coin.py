def coinChange(target, coins):
	dp = [0]*(target+1)
	dp[0] = 1
	
	for coin in coins:
		for i in range(coin, target+1):
			dp[i] += dp[i-coin]
	print(dp[-1])

	#or

	for j in range(1, target + 1):
		for coin in coins:
			if j >= coin:
				dp[j] += dp[j - coin]
	
	'''
	2 3 5 6
	
	2
	dp[0] =1
	dp[1] = 0
	dp[2] = 1
	dp[4] = 1
	dp[6] = 1
	dp[8] = 1
	dp[10] = 1
	

	dp[3] = 1
	dp[5] = 1
	dp[6] = 2
	dp[7] = 1
	dp[8] = 2
	dp[9] = 2


	아래 코드는 각 dp[j] = j를 만들수 있는 경우의 수라고 생각하면 된다.
	1과 2로	dp[4]의 (1 1 2) 랑(1 2 1) (2 1 1) (2 2) (1 1 1 1) 을 다 세는것 
	
    '''

    
def main():
	coins = [2, 5, 3, 6]

	coinChange(10, coins)

if __name__== '__main__':
	main()

