'''
오르막순
'''
'''
두번째풀이 
'''
n = int(input())
dp = [1]*10
for i in range(1,n) :
    for j in range(1,10) :
        dp[j] += dp[j-1]

print(sum(dp)%10007)
'''
첫번째풀이 - 시간초과남
'''
def solution():
    N = int(input())
    DP = [0 for _ in range(N+1)]
    nums = set()

    def check(num):
        for idx in range(1, len(num)):
            if int(num[idx]) >= int(num[idx-1]):
                continue
            else:
                return False
        
        return True


    
    for i in range(1,N+1):
        for j in range(10**i):
            if j not in nums:
                num = str(j)
                if check(num):
                    DP[i] += 1
    

    print(sum(nums[1:])%10007)

solution()
                


