'''
피보나치 수 6
'''
'''
세번째풀이 - 
'''
N = int(input())
mod = 1000000007
def fibo(n):
    if n <= 0:
        return 0
    
    if n == 1 or n == 2:
        return 1
    x = fibo(n//2 + 1) % mod
    y = fibo(n//2 - 1) % mod

    if n % 2 == 0:
        return x**2 - y**2
    
    elif n % 2 == 1:
        return x**2 + y**2

print(fibo(N))
'''
두번째풀이 - 분할정복시도했으나 틀림..
'''
# N = int(input())
# def fibo(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return fibo(n-1) + fibo(n-2) % 1000000007
# print(fibo(N))




'''
첫번째풀이 - 메모리초과
'''
# N = int(input())
# memo = [0,1]
# def fibo(n):
#     if n == 0:
#         return memo[0]
#     if n == 1:
#         return memo[1]
    
#     else:
#         for i in range(2,N+1):
#             memo.append((memo[i-1] + memo[i-2]) % 1000000007)
#     return memo[n]

# print(fibo(N))