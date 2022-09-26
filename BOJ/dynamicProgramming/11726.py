'''
2*N 타일링
'''
'''
두번째풀이
'''
def solution():
    N = int(input())
    dp = [0 for _ in range(10007)]
    dp[1] = 1
    dp[2] = 2
    mod = 10007
    
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    
    print(dp[N])
solution()

'''
첫번째풀이
'''
# def solution():
#     N = int(input())
#     DP = [0] * 1001
#     DP[1], DP[2] = 1, 2

#     for i in range(3, N+1):
#         DP[i] = DP[i-1] + DP[i-2]
    
#     return DP[N] % 10007
# print(solution())