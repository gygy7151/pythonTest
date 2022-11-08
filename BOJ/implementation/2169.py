'''
로봇조종하기
'''
'''
네번째풀이- G[i]를 할당하면 얕은 복사가 이루어져서 답이 올바르게 안나옴
반드시 G[i][:]를 해주어야됨
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    G = [ list(map(int, input().split())) for _ in range(N)]

    # 첫번째열
    for i in range(1, M):
        G[0][i] += G[0][i-1]
    
    # 나머지 열
    for i in range(1, N):
        # 아.. 앞으론 깊은 복사를 위해 슬라이싱 함수를 반드시 사용할것.
        left, right = G[i][:], G[i][:] #얕은복사가 이루어져서 문제였나봄.

        
        left[0] += G[i-1][0]
        for j in range(1,M):
            left[j] += max(left[j-1], G[i-1][j])

        right[M-1] += G[i-1][M-1]
        for j in range(M-2, -1, -1):
            right[j] += max(right[j+1], G[i-1][j])
        
        for k in range(M):
            G[i][k] = max(left[k], right[k])
    
    print(G[N-1][M-1])

solution()





'''
첫번째풀이- 틀림
'''
# from collections import deque
# def solution():
#     N, M = map(int, input().split())
#     DP = [[0 for _ in range(M)] for _ in range(N)]
#     G = [list(map(int,input().split())) for _ in range(N)]
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     visited[0][0] = 1
#     DP[0][0] = G[0][0]
#     q = deque()
#     q.append((0,0))

#     while q:
#         x, y = q.popleft()

#         for dx, dy in [(0,1), (0,-1), (1,0)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < M and 0 <= ny < N:
#                 if not visited[ny][nx]:
#                     visited[ny][nx] = 1
#                     DP[ny][nx] = max(DP[ny][nx], DP[y][x]+G[ny][nx])
#                     q.append((ny, nx))
    
#     print(DP[N-1][M-1])
# solution()