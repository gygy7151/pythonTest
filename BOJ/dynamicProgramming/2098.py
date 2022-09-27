'''
외판원 순회
'''
'''
1번 부터 N번까지의 도시들 존재
도시들 사이에는 길이 있을 수도 없을 수도 있따.
외판원이 한 도시에서 출발해 N개의 도시를 모두 거쳐 원래 출발한 도시로 돌아오는 여행경로 계획중임
단, 한번 갔던 도시로는 다시 갈 수 없음(물론 맨 마지막에 맨 처음 출발한 도시로 돌아오는것은 예외)
가장 적은 비용을 들이는 여행 계획을 세우고자 함
# i도시에서j 도시로 이동하는데 드는 비용 담긴 행렬 W[i][j]
# 단 W[i][j] != W[j][i] 있음에 주의. 항상 대칭적이지 않다.
# 모든 도시간의 비용은 양의 정수이고 W[i][i]는 항상 0이다.
# 경우에 다라 W[i][j] = 0인 경우도 존재함
# 항상 순회할 수 있는 경우만 입력으로 주어짐

# 진입차수가 필요하게꿈..
# 각 도시별로 다른 도시로 가는 비용이 담긴 graph
# 어떻게 풀것인가?
# i에서 j로 갈때 역으로 j에서 a..c로 갈 수 있으면
# a.. c에서 다시 d..f로 갈 수 있꼬 여기서 i가 있는지 없는지 매번 체크하면되지 않을까?
# dp필요할까? i가 있으면 해당 i값으로 하고 만약 i가 없으면 그중
# 
'''
'''
첫번째풀이 - 모르겠음..
'''
# from collections import deque
# def solution():
#     N = int(input())
#     G = []
    
#     answer = int(1e9)
    
#     for _ in range(N):
#         G.append(list(map(int, input().split())))

#     def bfs(start):
#         nonlocal answer
#         q = deque()
#         visit = [[0 for _ in range(N)] for _ in range(N)]




#         for idx, i in enumerate(G[n]):
#             if depth == N - 2 and:
#             dfs(i, depth+1, cost + G[n][idx])

'''
세번째풀이 - dp 초기값을 0으로 해주었다 INF가 아님
'''

#1 출발도시를 정한다
#2 거친 도시를 비트마스킹으로 표시한다
# 0001(2) = 1이라면 0번 도시만을 거침
# 0011(2) = 3이라면 0,1번도시를 거침
# 0111(2) = 7이라면 0,1,2번 도시를 거침
# 1111(2) = 15라면 0,1,2,3번 도시를 거침
# 이렇게 어느 도시들을 거쳤는지 거치지 않았는지를 비트마스크로 표시하였다.
#3  dp는 현재 도시에서 남은 도시들을 거쳐 다시 출발점으로 돌아오는 비용이 저장된다
# dp[cur][visit] = 현재 cur도시이며 방문현황은 visit와 같고, 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작지점으로 돌아가는데 드는 최소비용
# dp[0][0011(2)] = dp[0][3]은 현재 0번도시이며 0,1번 도시를 방문하였고, 2,3을 방문한후 다시 시작점으로 돌아갈때의 최소비용
# dp[2][0111(2)] = dp[2][7]은 현재 2번도시이며 0,1,2번 도시를 방문했다
# 즉 dp[0][0011] = dp[2][0111] + graph[0][2]가 되는 것이다.


n = int(input())
INF = int(1e9)
dp = [[0] * (1 << n-1) for _ in range(n)]

def dfs(x, visited):

    if dp[x][visited] != 0: # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    if visited == (1 << (n-1)) - 1: # 모든 도시를 방문했다면
        if graph[x][0]: # 출발점으로 가는 경로가 있을때
            return graph[x][0]
        
        else:
            # 순환경로가 없는경우 그냥 무한대로 값을 초기화해주어야한다.
            return INF
    min_dist = INF
    for i in range(1, n):
        if not graph[x][i]: #가는 경로가 없다면 skip
            continue
        if visited & (1 << i -1): # i번째도시를 이미 방문했다면 skip 
            continue

        dist = graph[x][i] + dfs(i, visited | (1 << (i - 1)))
        if min_dist > dist:
            min_dist = dist
    dp[x][visited] = min_dist
    
    return min_dist

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#0-indexed로 시작
print(dfs(0,0))

'''
두번째풀이
'''
import sys
input = sys.stdin.readline
n = int(input())
INF = int(1e9)
dp = [[0] * (1<<n) for _ in range(n)]

def dfs(x, visited):
    if visited == (1 << n) - 1: # 모든 도시를 방문했다면
        if graph[x][0]: # 출발점으로 가는 경로가 있을때
            return graph[x][0]
        
        else:
            # 순환경로가 없는경우 그냥 무한대로 값을 초기화해주어야한다.
            return INF

    if dp[x][visited] != 0: # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]
    
    min_dist = INF
    for i in range(1, n):
        if not graph[x][i]: #가는 경로가 없다면 skip
            continue
        if visited & (1 << i): # i번째도시를 이미 방문했다면 skip 
            continue

        dist = graph[x][i] + dfs(i, visited | (1 << (i)))
        if min_dist > dist:
            min_dist = dist
    dp[x][visited] = min_dist
    return min_dist

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#0-indexed로 시작
print(dfs(0,1))