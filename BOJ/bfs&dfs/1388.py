'''
바닥장식
'''
'''
세번째풀이
'''
# # dfs 알고리즘 함수 정의
# def dfs(x,y):
#     # 바닥 장식 모양이 '-' 일 때
#     if graph[x][y] == '-':
#         graph[x][y] = 1	    # 해당 노드 방문처리
#         for _y in [1,-1]:   # 양옆(좌우) 확인하기
#             Y = y + _y
#             # 좌우 노드가 주어진 범위를 벗어나지 않고 '-'모양이라면 재귀함수 호출
#             if (Y > 0 and Y < m) and graph[x][Y] == '-':
#                 dfs(x,Y)
#     # 바닥 장식 모양이 '|' 일 때
#     if graph[x][y] == '|':
#         graph[x][y] = 1	    # 해당 노드 방문처리
#         for _x in [1,-1]:   # 상하(위아래) 확인하기
#             X = x + _x  
#             # 상하 노드가 주어진 범위를 벗어나지 않고 '|' 모양이라면 재귀함수 호출
#             if (X > 0 and X < n) and graph[X][y] == '|':
#                 dfs(X,y)
 
# n,m = map(int, input().split()) # 방 바닥의 세로 크기 n, 가로 크기 m
# graph = []  # 2차원 리스트의 맵 정보 저장할 공간
# for _ in range(n):
#     graph.append(list(input()))
 
# count = 0
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == '-' or graph[i][j] == '|':
#             dfs(i,j)    # 노드가 '-'이나 '|'일 경우에 재귀함수 호출
#             count += 1
 
# print(count)

'''
두번째풀이 - 시간복잡도 O(N)
'''

def dfs(x,y):
    if graph[x][y] == '-':
        graph[x][y] = 1
        for _y in [1,-1]:
            Y = y +_y
            if(Y > 0 and Y < M) and graph[x][Y] == '-':
                dfs(x,Y)
            
        
    if graph[x][y] == '|':
        graph[x][y] = 1
        for _x in [1,-1]:
            X = x + _x
            if(X > 0 and X < N) and graph[X][y] == '|':
                dfs(x,y)
    
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

count = 0
for x in range(N):
    for y in range(M):
        if graph[x][y] =='-' or graph[x][y] == '|':
            dfs(x,y)
            count += 1

print(count)

'''
첫번째풀이 - 시간복잡도 O(N**2)
'''
# def solution():
#     N, M = map(int, input().split())
#     board = [list(input()) for _ in range(N)]
#     count = 0

#     #행
#     for i in range(N):
#         #열
#         j = 0
        
#         while j < M:
#             if board[i][j] == '|':
#                 j += 1
#             else:
#                 count += 1
#                 while j < M and board[i][j] == '-':
#                     j += 1
    
#     #열
#     for j in range(M):
#         #행
#         i = 0
        
#         while i < N:

#             if board[i][j] == '-':
#                 i += 1

#             else:
#                 count += 1
                
#                 while i < N and board[i][j] == '|':
#                     i += 1
        
        
#     print(count)

# solution()
