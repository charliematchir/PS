'''
Consider the below problems statement. There are 100 different types of caps each having a unique id from 1 to 100. Also, there are ‘n’ persons each having a collection of a variable number of caps. One day all of these persons decide to go in a party wearing a cap but to look unique they decided that none of them will wear the same type of cap. So, count the total number of arrangements or ways such that none of them is wearing the same type of cap. Constraints: 1 <= n <= 10. Since, number of ways could be large, so output modulo 1000000007
Time Complexity: O(n*2^n)
Auxiliary Space: O(n*2^n)
'''

from collections import defaultdict

class AssignCap:
    def __init__(self):
        self.allmask = 0
        self.total_caps = 100
        self.caps = defaultdict(list)
    
    def countWaysUtil(self, dp, mask, cap_no):
        if mask == self.allmask:
            return 1

        if cap_no > self.total_caps:
            return 0
        
        if dp[mask][cap_no] != -1:
            return dp[mask][cap_no]

        ways = self.countWaysUtil(dp, mask, cap_no +1)

        if cap_no in self.caps:
            for person in self.caps[cap_no]:
                if mask & (1<<person):
                    continue
                ways += self. countWaysUtil(dp, mask | (1<<person), cap_no +1)
                ways = ways %(1000000007)
        
        dp[mask][cap_no] = ways

        return dp[mask][cap_no]

    def countWays(self, N):
        for person in range(N):
            cap_possessed = map(int, raw_input().strip().split())
            for i in cap_possessed:
                self.caps[i].append(person)

        self.allmask = (1 << N) -1
        dp = [[-1 for j in range(self.total_caps + 1)] for i in range(2**N)]
        print(self.countWaysUtil(dp, 0, 1))

def main():
    Num_people = input()

    AssignCap().countWays(Num_people)

if __name__ == '__main__':
    main()



