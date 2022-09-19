'''
연구소3
'''
'''
연구소 3
'''

'''
두번째
'''
# from collections import deque
# from itertools import combinations
# import sys


# input = sys.stdin.readline
# inf = sys.maxsize

# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


# def bfs(active):
#     q = deque()
#     visited = [[-1] * n for _ in range(n)]
#     result = 0

#     for x, y in active:
#         q.append((x, y))
#         visited[x][y] = 0

#     while q:
#         x, y = q.popleft()

#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]

#             if 0 <= nx < n and 0 <= ny < n:
#                 if graph[nx][ny] == 0 and visited[nx][ny] == -1:
#                     q.append((nx, ny))
#                     visited[nx][ny] = visited[x][y] + 1
#                     result = max(result, visited[nx][ny])
#                 elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
#                     q.append((nx, ny))
#                     visited[nx][ny] = visited[x][y] + 1

#     if list(sum(visited, [])).count(-1) != wall_cnt:
#         return inf
#     return result


# wall_cnt = 0
# virus = []
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             wall_cnt += 1
#         elif graph[i][j] == 2:
#             virus.append((i, j))

# ans = inf
# for active in combinations(virus, m):
#     ans = min(ans, bfs(active))

# print(ans if ans != inf else -1)

# 연구소 bfs로 돌리고
# 값을 변경해서 벽1은 #으로바꾸고 바이러스 위치는 모두 q에 담는다.

# 모든 빈칸에 놓을 수 없는 경우는 어떻게 카운트를 할까? 바이러스를 어떻게 놓아도라..
# 각 바이러스가 어디에 놓여있든 상관없다는 말인거 같은데.. 그러면 하나라도 0이 존재 즉 빈칸이 존재하면 -1이 된다는거 아님?
# 0이 있을 확률을 구하는 걸 더블 체크를 해줘야 겠군
# 바이러스가 퍼질 수 있는 조건은 무엇인가? 1이 아니면 빈칸이든 바이러스가 놓일 수 있는 위치든 간에 상관없나봄
# 아 근데 바이러스를 한번에 하나씩만 놓을 수 있는건지 아니면 1개든 2개든 3개든 여러개를 놓을 수 있는건지 그게 궁금한데 여러개를 놓을 수 있는게 맞았음
# 심지어 같은 갯수라도 놓을 수 있는 모든 경우를 다 따져보아야 하는 거였음 아하...
# 그래서 틀린거였음 그럼 이건 조합을 활용해서 경우의 수를 모두 구해야 되는 거였음.

# 아 근데 바이러스는 처음엔 모두 비활성 상태라네..
# 근데 M개를 활성상태로 변경하려고 한다고 함. 아 문제를 대충 잘못 읽었네.. ㅋㅋㅋ
# M개가 정해져 있구나
# 연구소의 크기는 N임

from collections import deque
from itertools import combinations
def solution():
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    

    def bfs(unit):
        visit = [[-1 for _ in range(N)] for _ in range(N)]
        q = deque()
        result = 0
        
        for x, y in unit:
            q.append((x,y))
            visit[x][y] = 0


        while q:
            x, y = q.popleft()
            
            for dx, dy in [(0,1), (0, -1), (1,0), (-1,0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < N and 0 <= ny < N:
                    if visit[nx][ny] == -1 and graph[nx][ny] == 0:
                        q.append((nx, ny))
                        visit[nx][ny] = visit[x][y] + 1
                        result = max(result, visit[x][y] + 1)

                    # 활성바이러스가 비활성바이러스 위치로 가면 result 카운트에서 제외시켜준다. 단 방문표시는 한다
                    # 비활성화가 활성화 되는거기 때문에 그어떤 바이러스의 퍼짐현상도 없음 걍 상태값만 바뀌는거임
                    elif visit[nx][ny] == -1 and graph[nx][ny] == 2:
                        q.append((nx, ny))
                        visit[nx][ny] = visit[x][y] + 1
                        
        
        if list(sum(visit, [])).count(-1) != wall_cnt:
            return int(1e9)
        return result

    virus = []
    wall_cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                virus.append((i,j))
            
            elif graph[i][j] == 1:
                wall_cnt += 1


    answer = int(1e9)
    for unit in combinations(virus, M):
        answer = min(bfs(unit), answer)

    
    print(answer if answer != int(1e9) else -1)
solution()
                    



    

