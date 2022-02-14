'''
숨바꼭질 - 플로이드와샬 알고리즘 활용
전체맵에 M개의 양방향통로가 존재(이게플로이드와샬포인트였음)
전체노드는 연결되어 있음(이게플로이드와샬포인트였음)
'''
n, m = map(int, input().split())
INF = int(1e9)
#2차원 리스트를 만들고, 모든값을 무한으로 초기
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 초기화->하는이유가 굳이 26번부터29번코드필요없게끔하는거임.
for i in range(1, n+1):
    graph[i][i] = 0

#각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

distance= []
res = []
for i in range(1, n+1):
    min_dis = graph[1][i]
    distance.append((min_dis, i))
distance.sort()
max_dis = distance[-1][0]

for j in distance:
    if j[0] == max_dis:
        res.append(j[1])
res.sort()
print(res[0])
print(max_dis)
print(len(res))