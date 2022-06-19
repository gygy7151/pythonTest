'''
피보나치수5
'''
N = int(input())
memo = [0] * 10001
def fibo(n):
    if n == 0:
        return memo[0]
    if n == 1:
        memo[1] = 1
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(N))