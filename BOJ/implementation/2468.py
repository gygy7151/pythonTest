'''
안전영역
'''
'''
첫번째풀이 - 그 물에 잠기는 조건을 이상하게 27번줄처럼 생각해서 그랬음..
'''

from collections import deque

def solution():
    N = int(input())
    # 지역의 높이정보가 담긴 2차원 배열 G
    G = []
    maxHeight, minHeight = 0, 101
    for _ in range(N):
        data = list(map(int, input().split()))
        for height in data:
            if height > maxHeight:
                maxHeight = height
            
            if height < minHeight:
                minHeight = height
        
        G.append(data)
    
    if maxHeight == minHeight:
        #아.. 땅 높이가 1부터라는 거지 비높이는 범위 언급이 없어
            print(1)
            return
    
    else:
        # 안전영역 최대개수 answer
        answer = -1
        for rainHeight in range(minHeight, maxHeight):
            visited = [[0 for _ in range(N)] for _ in range(N)]

            def bfs(x,y):
                nonlocal visited
                q = deque()
                q.append((x,y))

                while q:
                    x, y = q.popleft()
                    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                        nx, ny = x + dx, y + dy
                        if  0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and G[nx][ny] > rainHeight:
                                visited[nx][ny] = 1
                                q.append((nx,ny))
            
            safeRegionCnt = 0
            for i in range(N):
                for j in range(N):
                    if not visited[i][j] and G[i][j] > rainHeight:
                        bfs(i,j)
                        safeRegionCnt +=1
            
            if safeRegionCnt > answer:
                answer = safeRegionCnt

        print(answer)

solution()



