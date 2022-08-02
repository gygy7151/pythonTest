'''
숨바꼭질2
'''
'''
첫번째풀이
'''
from collections import deque

def solution():
    MAX = 100001
    visited = [ [-1,0] for _ in range(MAX)]

    N, K = map(int, input().split())
    q = deque()
    q.append(N)
    # 최단거리 경우의 수 수학적 개념 알고있으면 이해가 빠름
    visited[N][0] = 0
    visited[N][1] = 1

    while q:
        now = q.popleft()

        for new in [now*2, now+1, now-1]:
            
            #범위제한
            if 0 <= new < MAX:
                #처음들르는경우
                if visited[new][0] == -1:
                    visited[new][0] = visited[now][0] + 1
                    visited[new][1] = visited[now][1]
                    q.append(new)

                #한번 이상 들르는 경우            
                elif visited[new][0] == visited[now][0] + 1:
                    visited[new][1] += visited[now][1]
    
    print(visited[K][0])
    print(visited[K][1])
solution()

    




