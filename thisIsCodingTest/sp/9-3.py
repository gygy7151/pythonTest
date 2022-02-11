'''
플로이드 워셜 알고리즘 소스코드
'''
INF = int(1e9)

#노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

#2차원 리스트를 만들고, 모든값을 무한으로 초기
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 초기화->하는이유가 굳이 26번부터29번코드필요없게끔하는거임.
for i in range(1, n+1):
    graph[i][i] = 0

#각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

#수행된 결과를 출력
for i in range(1, n+1):
    for j in range(1, n+1):
    #도달할 수 없는 경우 , 무한
        if graph[i][j] == INF :
            print('INFINITY', end = " ")
    # 도달 할 수 있는 경우 거리를 출력
        else:
            print(graph[i][j], end =" ")
    #노드구분
    print()