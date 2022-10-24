'''
단지 번호 붙이기
'''
'''
첫번째풀이
'''
from collections import deque

def solution():
    N = int(input())
    G = [list(input()) for _ in range(N)]
    answer = []
    visited = [[0 for _ in range(N)] for _ in range(N)]

    def bfs(x,y):
        nonlocal visited
        q = deque()
        q.append((x,y))
        # 초기 시작점 포함
        cntHouse = 1
        
        while q:
            x, y = q.popleft()
            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    # 집 존재 여부가 숫자가 아닌 str 타입을 주의하자..
                    if not visited[nx][ny] and G[nx][ny] == '1':
                        visited[nx][ny] = 1
                        q.append((nx,ny))
                        cntHouse += 1
        return cntHouse


    for i in range(N):
        for j in range(N):
            # 단순히 방문만 안한게 아니라 그래프에 특정값이 맞는지 확인해주어야했다.
            if not visited[i][j] and G[i][j] == '1':
                visited[i][j] = 1
                answer.append(bfs(i,j))
    print(len(answer))
    # 아..오름차순 주의.. 항상 최종 제출하기전에 출력조건 잘 맞췄는지 코드로 확인할것!! 테스트코드결과말고..
    print(*sorted(answer), sep="\n")
solution()
