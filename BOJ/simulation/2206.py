'''
벽부수고 이동하기
='''
'''
세번째풀이 - 2차원 배열로 접근시 시간초과남. 그리고 단순히 3개이상 1이 둘러쌓였다고 벽을 뚫어버리면 다른경우엔 안되는 경우도 있음
벽을 부수고 온 경우가 벽을 부수지 않고 오는 경우보다 먼저 방문하게 된다면,
이는 불가능으로 판단하여 -1출력한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    MAP = []
    for _ in range(N):
        MAP.append(list(map(int, list(input().strip()))))
    
    def bfs():
        dir = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque()
        q.append([0,0,1])

        #방문체크를 2가지 케이스로 나눠서 진행해야함
        #[0,0] = 벽을 부수고 이동하는 경로, 벽을 부수지 않고 이동하는 경로 각각 따로 저장한다.
        visit = [[[0] * 2 for _ in range(M)] for i in range(N)]

        #처음엔 벽을 부수지 않고 이동하는 경로로 이동을 시작한다
        visit[0][0][1] = 1

        while q:
            # w는 wall의 약자.
            x, y, w = q.popleft()
            if x == N - 1 and y == M - 1:
                return visit[x][y][w]
            
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    
                    # 벽을 부수고 이동
                    if MAP[nx][ny] == 1 and w == 1:
                        visit[nx][ny][w-1] = visit[nx][ny][w] + 1
                        q.append([nx,ny,w-1])

                    # 벽을 부수지 않고 이동
                    if MAP[nx][ny] == 0 and visit[nx][ny][w] == 0:
                        visit[nx][ny][w] = visit[x][y][w] + 1
                        q.append([nx,ny,w])
        else:
            return -1
    
    print(bfs())

solution()


from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input())) for _ in range(n)]

visitied = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx,dy = [-1,0,1,0],[0,-1,0,1]

def solution(x,y,break_one_wall,visitied,graph):
    queue = deque()
    queue.append((x,y,break_one_wall))
    visitied[x][y][break_one_wall] = 1
    while queue:
        x,y,break_one_wall = queue.popleft()
        if x == n-1 and y == m-1:
            return visitied[x][y][break_one_wall]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            #벽을 부수지 않고 이동
            if graph[nx][ny] == 0 and visitied[nx][ny][break_one_wall]==0:
                queue.append((nx,ny,break_one_wall))
                visitied[nx][ny][break_one_wall] = visitied[x][y][break_one_wall]+1
            if graph[nx][ny] == 1 and break_one_wall == 1:
                queue.append((nx,ny,break_one_wall-1))
                visitied[nx][ny][break_one_wall-1] = visitied[x][y][break_one_wall]+1
    return -1
print(solution(0,0,1,visitied,graph))
    

'''
첫번째/두번째풀이 - q에 넣는 수 타입 주의, 범위제한 조건 삭제 - '2'로 범위 아예 확장시킴
'''
# import sys
# input = sys.stdin.readline
# from collections import deque

# def solution():
#     N, M = map(int, input().split())
#     MAP = [['1' for _ in range(M+2)]]
    
#     for _ in range(N):
#         MAP.append( ['1'] + list(input().strip()) + ['1'])
    
#     MAP.append(['1' for _ in range(M+2)])
#     answer = []

#     if N == 1 and M == 1:
#         print(1)
#         return

#     def break_bfs():
#         nonlocal answer
#         q = deque()
#         q.append((1,1,1))
#         dir = [(1,0), (-1,0), (0,1), (0,-1)]
#         chance = 1

#         MAP[1][1] = '1'

#         while q:
#             x, y, count = q.popleft()

#             #x,y는 정수임. 문자가 아님 주의
#             if x == N and y == M:
#                 answer.append(count)
#                 break
            
#             # 벽을 부수고 이동하는 찬스
#             allImpossible = 0

#             for dx, dy in dir:
#                 nx, ny = x+dx, y+dy
#                 if x == 3 and y == 4:
#                     print(nx,ny)
                
#                 if 1 <= nx <= N and 1 <= ny <= M:
#                     if MAP[nx][ny] == '0':
#                         q.append((nx,ny,count+1))
#                         print(q)
#                         MAP[nx][ny] = '1'
                    
#                     else:
#                         allImpossible += 1
            
#             if allImpossible >= 3 and chance == 1:
#                 chance = 0
#                 for dx, dy in dir:
#                     nx, ny = x+dx, y+dy
#                     if 1 <= nx <= N and 1 <= ny <= M:
#                         if MAP[nx][ny] == '1':
#                             q.append((nx,ny,count+1))
#                             print(q)
#                             MAP[nx][ny] = '1'

#         else:
#             answer.append(-1)

    
#     break_bfs()
#     print(max(answer))
# solution()
        
