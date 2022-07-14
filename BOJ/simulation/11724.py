'''
연결 요소의 개수
'''
'''
세번째풀이 - bfs로접근 - deque안사용해도 시간초과해결 ***상당히 헷갈렸음..
'''
# import sys
# input = sys.stdin.readline
# def solution():
#     N, M = map(int, input().split())
#     T = [[] for _ in range(N+1)]
#     MEMO = [0] * (N+1)
#     count = 0

#     for _ in range(M):
#         A, B = map(int, input().split())
#         T[A].append(B)
#         T[B].append(A)
    
#     def bfs(v):
#         Q = [v]
#         MEMO[v] = 1

#         while Q:
#             node = Q.pop(0)

#             #bfs해당노드에 바로 접근하기때문에 연결노드 모두를 확인할 수 있다.
#             #이점이 바로 내가 처음짰던 코드와 차이점임
#             for edege in T[node]:
#                 if MEMO[edege] == 0:
#                     Q.append(edege)
#                     MEMO[edege] = 1
    
#     for i in range(1, N+1):
#         if MEMO[i] == 0:
#             bfs(i)
#             count += 1
    
#     print(count)
# solution()


'''
두번째풀이..아.. 트리가 아닌데 트리로 접근했다..
'''
# def solution():
#     N, M = map(int, input().split())
#     T = [[] for _ in range(N+1)]
#     MEMO = [0] * (N+1)

#     for _ in range(M):
#         A, B = map(int, input().split())
#         T[A].append(B)
#         T[B].append(A)
    
#     ANS = 0
#     for i in range(1,N+1):
#         Q = []
#         if MEMO[i] == 0:
#             Q.append(i)
#         while Q:
#             A = Q.pop(0)
#             for B_idx in range(len(T[A])):
#                 B = T[A][B_idx]
                
#                 if MEMO[B] == 0:
#                     MEMO[B] =  A
#                     Q.append(B)

#                 elif MEMO[B] == i:
#                     ANS += 1
#                     break
                    
            
#     print(MEMO)
#     print(ANS)
# solution()


'''
첫번째풀이 -틀림 이미 4번노드를 한번 방문하면 해당 노드와 연결된 노드를 확인할 수가 없다.
아님.. 내가 방문한 인접노드를 vistied에 안넣고 부모노드만 집어넣어서 그런거임..
사실 올바른 풀이였음
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    LINK = [[] for _ in range(N+1)]
    SET_CNT = 0

    for _ in range(M):
        U, V = map(int, input().split())
        LINK[U].append(V)
        LINK[V].append(U)
    
    MEMO = [0 for _ in range(N+1)]


    for i in range(1, N+1):
        visited = []

        if MEMO[i] == 0:
            visited.append(i)
            MEMO[i]
            while visited:
                node = visited.pop(0)

                for link in LINK[node]:
                    
                    if MEMO[link] == 0:
                        #아..여기에 node가 아니라 link를 넣었어야했다...
                        visited.append(link)
                        MEMO[link] = 1
                
            SET_CNT += 1

    return SET_CNT
print(solution())