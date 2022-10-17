'''
알고스팟
'''
'''
첫번째풀이 - 다익스트라로 풂, 힙으로 대용량 노드에 따른 시간초과 해결
'''
import heapq


def solution():
    M, N = map(int, input().split())
    # 미로의 상태를 나타내는 2차원 배열 maze
    maze = []
    
    for _ in range(N):
        maze.append(list(map(int, list(input()))))
    
    # 부수어야 하는 벽의 개수 정보를 담은 2차원 배열 wall
    wall = [[-1 for _ in range(M)] for _ in range(N)]
    wall[0][0] = 0
    q = []
    heapq.heappush(q, (0, (0,0))) #벽의 개수, 이동좌표
    
    visited = [[0 for _ in range(M)] for _ in range(N)]

    while q:
        wall_cnt, pos = heapq.heappop(q)
        x, y = pos

        if wall[x][y] < wall_cnt:
            continue

        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:

                # 빈 방일때와 벽일때의 방을 구분해서 부수어야할 벽의 개수를 wall에 갱신한다.
                # 빈방일때
                distance = maze[nx][ny]
                wall[nx][ny] = wall[x][y] + distance
                # if maze[nx][ny] == 0:
                #     wall[nx][ny] = wall[x][y] + 0
                # # 벽일때
                # else:
                #     wall[nx][ny] = wall[x][y] + 1

                heapq.heappush(q, (wall[nx][ny], (nx,ny)))
                visited[nx][ny] = 1
        
    print(wall[N-1][M-1])
    

solution()
                


            
                



