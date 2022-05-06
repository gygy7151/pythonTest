'''
이항계수3
'''
'''
두번째풀이
'''
import sys
input = sys.stdin.readline

def square(n,k):
    if k == 0:
        return 1
    if k % 2:
        return (square(n, k//2)** 2 * n) % p
    else:
        return (square(n, k//2) ** 2) % p
    
N, K = map(int, input().split())
p = 1000000007

f = [1 for _ in range(N+1)]
for i in range(2, N+1):
    f[i] = f[i-1] * i % p

a = f[N]
b = f[N-K] * f[K] % p
print((a%p) * ((square(b, p-2))% p) % p)




'''
첫번째풀이 - 틀림, 및 dp로 푸는게 더 나음, 그리고 페르마의 소정리 활용해야됨 Ndl 너무 큰 숫자라 오버플로우 걸림
'''
# import sys
# input = sys.stdin.readline
# def factorial(n):
#     ans = 0
#     for i in range(2, n+1):
#         ans *= i    
#     return i
# n, k = map(int, input().split())
# b = 1000000007
# a = factorial(n) / (factorial(n-k) * factorial(k))
# res = a % b
# print(res)
