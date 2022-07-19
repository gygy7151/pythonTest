'''
피보나치수-우와..
'''
def fibo(n):
    dp = [ i for i in range(n+1)]
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fibo(int(input())))

'''
두번째풀이 -시간초과
'''
# memo = [0,1] + [0]* 45
# def fibo(n):
#     if n in[1,0]:
#         return memo[n]
#     memo[n] = memo[n-1] + memo[n-2]
#     return memo[n]
# print(fibo(int(input())))
'''
첫번째풀이 - 시간초과
'''
# def fibo(n):
#     if n <= 2:
#         return 1
    
#     return fibo(n-1) + fibo(n-2)
# n = int(input())
# print(fibo(n))