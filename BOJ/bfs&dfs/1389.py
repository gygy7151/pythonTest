'''
케빈 베이컨의 6단계 법칙
'''
'''
세번째풀이
'''
#조금더 간단하게 end랑 같은 노드발견하면 바로 return해주는걸로 수정
import sys
input = sys.stdin.readline
from collections import deque

def solution():
    N, M = map(int, input().split())
    #1번째 인덱스부터 사용하기 위해 N+1
    LINK = [[False for _ in range(N+1)] for _ in range(N+1)]
    
    for _ in range(M):
        friendA, friendB = map(int ,input().split())
        LINK[friendA][friendB] = True
        LINK[friendB][friendA] = True
    
    def bfs(start,end):
        q = deque()
        # 0은 시작단계를 의미
        q.append((start,0))
        final_step = 0
        
        while q:
            friendA, step = q.popleft()
            for friendB in range(1,N+1):
                
                if LINK[friendA][friendB] == True:
                
                    if friendB == end:
                        final_step = step
                        return final_step

                    else:
                        q.append((friendB, step + 1))
                        final_step = step + 1
    ANS = []
    cnt = 0
    
    for i in range(1,N+1):
        cnt = 0
        for j in range(1,N+1):
            cnt += bfs(i,j)
        
        ANS.append((cnt,i))
    
    ANS.sort(key=lambda x: (x[0], x[1]))
    return ANS[0][1]

print(solution())

'''
첫번째/두번째풀이 - 출력형식을 제대로 확인안하고 제출했음 제일작은 사람의 번호를 출력하는거임
'''
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solution():
#     N, M = map(int, input().split())
#     #1번째 인덱스부터 사용하기 위해 N+1
#     LINK = [[False for _ in range(N+1)] for _ in range(N+1)]
    
#     for _ in range(M):
#         friendA, friendB = map(int ,input().split())
#         LINK[friendA][friendB] = True
#         LINK[friendB][friendA] = True
    
#     def bfs(start,end):
#         q = deque()
#         # 0은 시작단계를 의미
#         q.append((start,0))
#         final_step = 0
#         end_find = False
        
#         while q:
#             friendA, step = q.popleft()
#             for friendB in range(1,N+1):
                
#                 if LINK[friendA][friendB] == True:
                
#                     if friendB == end:
#                         end_find = True
#                         final_step = step
#                         break

#                     else:
#                         q.append((friendB, step + 1))
#                         final_step = step + 1

#             if end_find:
#                 return final_step

#     ANS = []
#     cnt = 0
    
#     for i in range(1,N+1):
#         cnt = 0
#         for j in range(1,N+1):
#             cnt += bfs(i,j)
        
#         ANS.append((cnt,i))
    
#     ANS.sort(key=lambda x: (x[0], x[1]))
#     return ANS[0][1]

# print(solution())