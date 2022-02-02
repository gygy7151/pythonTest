'''
미래도시
방문판매원 A는 많은 회사가 모여있는 공중미래도시에 있다
공중 미래 도시에는 1번부터 N번까지의 회사가 있는데 = N개의 노드
특정회사끼리는 서로 도로를 통해 연결되어 있음 = 간선이 몇개냐?모름
방문판매원 A는 현재 1번회사에 위치, x번 회사에 방문해 물건을 판매하고자 한다
2개의 회사는 양방향으로 이동가능함
소개팅상대는 k번회사에 존재함
1 -> K -> X ->거쳐가는거면 1+k랑 k+x랑 모두 구해야 되는거니까 플로이드와샬로 풀어줘야됨
회사가 연결되어 있으면 무조건 1만큼의 시간이 걸림 = 거리가 1이라는 의미.
위 이동거리 최소시간 계산프로그램을 만드시오
이때 소개팅의 상대방과 커피마시는 시간은 고려하지 않음
N = 5, X = 4, K = 5이고, 도로가 7개면
첫째줄에 전체회사의 개수 N과 경로의개수 M입력
둘째줄부터 M+1번째줄에는 연결된 두 회사의 번호가 공백으로..
M+2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어짐

출력조건 A가 k번 회사를 거쳐 x번회사로 가는 최소이동시간을 출력시
도달할 수 없다면 -1을 출력한다.
'''
INF = int(1e9)
n,m= map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    #서로가 가는비용은 1임
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for s in range(1, n+1):
            graph[j][s] = min(graph[j][s], graph[j][i]+graph[i][s])


distance = graph[1][k] + graph[k][x]

if distance >= INF:

    print("-1")

else:
    print(distance)
        
