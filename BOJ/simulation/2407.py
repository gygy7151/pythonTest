'''
조합
'''
'''
첫번째풀이
'''
def factorial(n):
    if n == 0:
        return 1
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer

def solution():
    N, M = map(int, input().split())
    answer = factorial(N) // (factorial(N-M) * factorial(M))
    print(answer)
solution()