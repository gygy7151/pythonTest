'''
1로 만들기
'''
'''
세번째풀이 - 초기값을 0으로 설정
'''
def solution():
    N = int(input())
    DP = [0 for _ in range(N+1)]

    for i in range(2, N+1):

        # i-1한값으로 초기화
        DP[i] = DP[i-1] + 1

        if i % 3 == 0:
            DP[i] = min(DP[i//3]+1, DP[i])

        if i % 2 == 0:
            DP[i] = min(DP[i//2]+1, DP[i])
        
    return DP[N]
print(solution())
        
'''
첫번째/두번째풀이 - 초기값을 매우 큰수로 설정한 풀이
'''
# def solution():
#     N = int(input())
#     DP = [int(1e9) for _ in range(N+1)]
#     # print(DP)
#     if N == 2 or N == 3 or N == 5:
#         return 1
#     elif N == 1:
#         return 0
#     else:
#         DP[2], DP[3] = 1, 1

#     for i in range(4, N+1):

#         if i % 5 == 0:
#             DP[i] = min(DP[i//5] + 1, DP[i])

#         if i % 3 == 0:
#             DP[i] = min(DP[i//3] + 1, DP[i])

#         if i % 2 == 0:
#             DP[i] = min(DP[i//2] + 1, DP[i])

#         DP[i] = min(DP[i-1] + 1,DP[i])
#     # print(DP)
#     return DP[i]

# print(solution())