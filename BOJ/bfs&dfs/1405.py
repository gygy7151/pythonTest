'''
미친로봇
'''
'''
두번째풀이 - dfs와 백트래킹 사용
dfs 풀이고 visted를 해주어야했음을 깜빡함. 왜냐 이미 지나갔던 길을 되돌아가지 않아야 하기 때문에
'''
import sys
input = sys.stdin.readline
d = [(0,1), (0,-1), (1,0),(-1,0)] 

def dfs(r, c, visited, total):
    global answer
    # dfs 종료조건은 visited의 길이는 시작점을 표현하여 N+1이면 종료
    if len(visited) == N+ 1:
        answer += total
        return

    # 4방향으로 이동 
    for idx in range(4):
        #  방향 오타 주의 ㅠ
        nr, nc = r + d[idx][0], c + d[idx][1]

        #이동하는 좌표가 visited에 존재 안하면 visited에 추가하고 재귀돌림
        ## 아..어차피 그래프 제한이 범위제한 없었음
        # dfs를 진행하면서 동서남북에 알맞는 확률을 곱해주면서 진행한다.
        if (nr,nc) not in visited:
            visited.append((nr,nc))
            dfs(nr, nc, visited, total * dir[idx])
            # 다음 방향 탐색을 위해 추가한 좌표는 바로 pop해준다
            visited.pop()
        
N, e, w, s, n = map(int, input().split())
dir = [e, w, s, n] # dir값도 d와 반드시 일치할 필요가 없었음.
answer = 0
# 재귀 종료시 asnwer 변수에 지금까지 누적한 확률을 더해준다.
dfs(0,0, [(0,0)], 1)
# 주어진 확률은 %단위로 주어졌기 때문에 answer에 0.01 ** N을 곱해주고 출력한다
print(answer * (0.01** N)) # 괄호주의








'''
첫번째풀이 - 도저히 모르겠다.. 틀림.
'''
# # 단순한걸 어떻게 구하니? 같은곳을 한번보다 많이 이동하지 않을때 단순하다고 함
# import sys
# input = sys.stdin.readline

# N, e, w, s, n = list(map(int, input().split()))

# # 이동하는 곳의 방향을 표시하기 위해 따로 이렇게 필요함
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# #동, 서, 남, 북에 맞춰 값들을 넣어줌
# percent_data = [e,w,s,n]

# #주어진 N을 기점으로 N,N이 한가우데 오는 2차원 배열을 만들어줌
# graph = [[0 for _ in range(2*N+1)] for _ in range(2*N+1)]

# answer = 0

# def dfs(x,y,percent,cnt):
#     # 전역 변수로 만들어서 모든 dfs가 함수 실행될때 cnt == N이면 answer에 확률을 더하게 됨
#     global answer
#     if cnt == N:
#         #확률은 더해주는거. 곱하는게 아님
#         answer += percent
#         return
    
#     #현재 좌표의 확률을 now_percent에 담아둔다
#     now_percent = percent

#     #방문처리
#     graph[x][y] = 1

#     for i in range(4):
#         nx, ny = x+dx[i], y +dy[i]

#         # 이미 방문했으면 continue
#         if graph[nx][ny] == 1:
#             continue

#         # 방문안했으면 이동할 좌표, 이동하는 곳의 확률을 현재 확률에 곱해주고 cnt + 1해준다.
#         else:
#             # 동서남분 순서에 따라 percent_data를 맞춰준다. 곱할땐 100으로 나눠서 계산
#             dfs(nx,ny, now_percent*(percent_data[i]/100), cnt+1)
#             #dfs 실행하고, 다른 dfs 함수의 실행을 위해 방문처리를 해제해준다.
#             graph[nx][ny] = 0

# dfs(N,N,1,0)
