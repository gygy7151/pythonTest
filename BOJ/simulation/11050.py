'''
이항계수
'''
'''
다섯번째 풀이 - top-down방식.
마치 일주일동안 커피를 마실날을 결정하는 것은
일주일동안 커피를 마시지 않을 날을 결정하는 것과 같다.
본질적으로 똑같다.
'''
def solution(n,k):
    if k > n:
        return 0

    MEMO = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    def pick(times, left):
        if times == 0:
            return left == 0
        
        if MEMO[times][left] != -1:
            return MEMO[times][left]
        
        MEMO[times][left] = pick(times-1, left) + pick(times-1, left-1)
        
        return MEMO[times][left]
    
    return pick(n,n-k)

N, K = map(int, input().split())
print(solution(N,K))



'''
네번째풀이 - 확률이나 통계등의 확장성응용 - bottom-up방식
'''
# def solution(n,k):
#     if k > n:
#         return 0
#     MEMO = [[-1 for _ in range(n+1)] for _ in range(n+1)]

#     def pick(times, got) :
#         if times == n:
#             # 선택한개수(=got)이 k개가되면 1을반환하고 아니면 0을 반환함
#             return got == k
        
#         if MEMO[times][got] != -1:
#             return MEMO[times][got]
        
#         MEMO[times][got] = pick(times+1, got) + pick(times+1, got+1)
#         return MEMO[times][got]
    
#     # bottom - up
#     return pick(0,0)

# N, K  = map(int, input().split())
# print(solution(N,K))

'''
세번째풀이 - 캐쉬활용
'''
# def solution(n,k):
#     MEMO = [[0 for _ in range(k+1)] for _ in range(n+1)]

#     for i in range(n+1):
#         MEMO[i][0] = 1
#     for j in range(k+1):
#         MEMO[j][j] = 1
    
#     for i in range(1, n+1):
#         for j in range(1, k+1):
#             MEMO[i][j] = MEMO[i-1][j] + MEMO[i-1][j-1]
    
#     return MEMO[n][k]

# N, K = map(int, input().split())
# print(solution(N,K))

'''
두번째풀이 - 간단한 재귀활용. but 부분문제 중복 해결안됨
'''
# def solution(n,k):
#     if k == 0 or n == k:
#         return 1
#     return solution(n-1,k) + solution(n-1,k-1)

# N,K = map(int, input().split())
# print(solution(N,K))
'''
첫번째풀이 - 구현
'''
# def factorial(n):
#     ans = 1
#     if n <= 1:
#         return 1
#     for i in range(2, n+1):
#         ans *= i
#     return ans

# def solution(n,k):
#     return factorial(n) // factorial(k) // factorial(n-k)

# N,K = map(int, input().split())
# print(solution(N,K))