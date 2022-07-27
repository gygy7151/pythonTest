'''
정수삼각형
'''
'''
네번째풀이
'''
'''
왼쪽 대각선 방향에서 T[i-1][j-1]해야했는데 T[i-1][j]로 작성하는 실수를 범함
두번째 for문 범위에서 2번째 행부터 접근하므로 너비를 올바르게 지정해주어야 하는데
1부터 지정해줘서 잘못구해졌음 len(T[i])로 수정하고 맨끝요소도 len(T[i])-1로 해주거나 
아니면 j == i로 해주어야되었음
'''
def solution():
    T = []
    N = int(input())
    for _ in range(N):
        T.append(list(map(int, input().split())))

    for i in range(1,N):
        for j in range(i+1):
            if j == 0:
                T[i][j] = T[i-1][j] + T[i][j]

            elif j == i:
                T[i][j] = T[i-1][j-1] + T[i][j]
            
            else:
                T[i][j] = max(T[i-1][j-1], T[i-1][j]) + T[i][j]
    
    return max(T[N-1])
print(solution())

'''
세번째풀이 - 틀림
'''
# def solution():
#     T = []
#     N = int(input())
#     for _ in range(N):
#         T.append(list(map(int, input().split())))

#     for i in range(1,N):
#         for j in range(len(T[i])):
#             if j == 0:
#                 T[i][j] = T[i-1][j] + T[i][j]

#             elif j == len(T[i])-1:
#                 T[i][j] = T[i-1][j] + T[i][j]
            
#             else:
#                 T[i][j] = max(T[i-1][j-1], T[i-1][j]) + T[i][j]
    
#     return max(T[N-1])
# print(solution())



'''
두번째풀이 - DP -틀림
'''
# def solution():
#     N = int(input())
    
#     if N == 1:
#         return int(input())
    
#     DP = [[] for _ in range(N)]
#     DP[0].append(int(input()))
    
#     for i in range(1,N):
#         try:
#             data = list(map(int, input().split()))
        
#             for j in range(i):
#                 if j == 0:
#                     DP[i].append(data[j] + DP[i-1][0])

#                 if j == i-1:
#                     DP[i].append(data[j] + DP[i-1][i-1])
                
#                 else:
#                     DP[i].append( max(data[j]+DP[i-1][j-1], data[j]+DP[i-1][j]) )
#         except:
#             pass

#     return max(DP[N-1])

# print(solution())

'''
첫번째풀이 - 메모리 초과
'''
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solution():
#     answer = -1
#     tri = []
    
#     for _ in range(int(input())):
#         tri.append(list(map(int, input().split())))

#     def bfs():
#         nonlocal answer
#         q = deque([(tri[0][0],0,0)])
        
#         while q:
#             num, idx, flr = q.popleft()
#             try:
#                 if tri[flr+1]:
#                         if num + tri[flr+1][idx] > answer:
#                             q.append((num+tri[flr+1][idx], idx, flr+1))
#                         if num + tri[flr+1][idx+1] > answer:
#                             q.append((num+tri[flr+1][idx+1], idx+1, flr+1))
#             except:
#                 answer = max(num, answer)
#     bfs()
#     print(answer)
# solution()



