'''
연구소
'''
'''
첫번째풀이
bfs, 시작점 여러개임
'''
# 벽을 3개씩 세우는걸 어케할까? 조합을 사용하는 방법이 있을꺼임
# 우선 조합으로라도 해볼까?
# 모든 바이러스를 미리 큐에 넣는다.
from collections import deque
from itertools import combinations
import copy
def solution():
    N, M = map(int, input().split())
    graph = []
    canBeWall = []
    virus = []

    for y in range(N):
        data = list(map(int, input().split()))
        for x in range(M):
            if data[x] == 0:
                canBeWall.append((y,x))
            if data[x] == 2:
                virus.append((y,x))
        graph.append(data)
                
    setWall = list(combinations(canBeWall, 3))

    def checkCnt(G):
        answer = 0
        for y in range(N):
            for x in range(M):
                if G[y][x] == 0:
                    answer += 1
        
        return answer

    def bfs(G):
        q = deque()
        q.extend(virus)

        while q:
            y, x = q.popleft()
            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if G[ny][nx] == 0:
                        G[ny][nx] = 2
                        q.append((ny,nx))

        return checkCnt(G)

    maxSize = 0
    for wallThree in setWall:
        temp = copy.deepcopy(graph)
        for y, x in wallThree:
            temp[y][x] = 1
        res = bfs(temp)

        if maxSize < res:
            maxSize = res
    
    print(maxSize)

solution()
            
