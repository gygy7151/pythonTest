'''
경로찾기
'''
'''
첫번째풀이
'''
import sys
from collections import deque

def solution():
    N = int(input())
    
    G = [list(map(int, input().split())) for _ in range(N)]

    if N == 1:
        #여기서 타입에러난거예상.
        return G
    
    def bfs(start, end):
        Q = deque()
        Q.append(start)
        # **실수(연결된 노드를 방문처리확인을 안하면 무한루프에 빠짐)
        visited = [False for _ in range(N)]

        while Q:
            v = Q.popleft()
            visited[v] = True

            for i in range(len(G[v])):
                
                if G[v][i] == 1:
                
                    if i == end:
                        return True
                    else:
                        #방문하지 않은 노드만 방문할 수 있도록 예외처리 적용
                        if not visited[i]:
                            #연결된노드삽입
                            Q.append(i)
        
        return False
    
    ANS = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if bfs(i,j):
                ANS[i][j] = 1

    return ANS
res = solution()
for r in res:
    print(*r)