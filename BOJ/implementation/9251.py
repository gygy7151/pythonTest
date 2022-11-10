'''
LCS
'''
'''
세번째풀이 -  굳이 갯수를 따로 셀개 아니라 graph안에 표기하는 방법을 활용함 이게 바로 DP임
# '''
def solution():
    A, B = input(), input()
    N, M = len(A), len(B)
    DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            #아... 입력문자열은 0-indexed였다. 주의
            if A[i-1] == B[j-1]: 
                DP[i][j] = DP[i-1][j-1] + 1
            
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])


    print(DP[-1][-1])

solution()
# def solution():
#     A, B = input(), input()
#     N, M = len(A), len(B)

#     dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

#     for r in range(1, N+1):
#         for c in range(1, M+1):
#             if A[r-1] == B[c-1]:
#                 dp[r][c] = 1 + dp[r-1][c-1]
            
#             else:
#                 dp[r][c] = max(dp[r-1][c], dp[r][c-1])
    
#     return dp[-1][-1]
# print(solution())





'''
두번째풀이 -  DP는 아니지만 이전값을 활용해서 풀어봄
'''
# def solution():
#     StrA, StrB = input(), input()
#     graph = [[0 for _ in range(len(StrA))] for _ in range(len(StrB))]

#     # 일치하는것 모두 1로 초기화
#     for b in range(len(StrB)):
#         for a in range(len(StrA)):
#             if StrA[a] == StrA[b]:
#                 graph[b][a] = 1

#     # 일치하는 것이 나타나면 j범위를 좁혀줌
#     j = 0
#     answer = 0
#     for a in range(len(StrB)):
#         for b in range(j, len(StrA)):
#             if StrA[a] == StrB[b]:
#                 j = b+1
#                 answer += 1
#                 break
    
#     print(answer)
# solution()
    




    




'''
첫번째풀이- DP로 안풀어서 틀림
'''
# def solution():
#     A, B = input(), input()
#     i, j = 0, 0
#     answer = 0
#     while True:
#         if i == len(A)-1:
#             break
#         if A[i] == B[j]:
#             answer += 1
#             i += 1
#         else:
#             if j == len(B) - 1:
#                 i+= 1
#                 continue
#             j += 1
    
#     print(answer)
# solution()
