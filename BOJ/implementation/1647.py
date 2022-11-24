'''
도시분할계획
'''
'''
두번째풀이
'''
import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    # 이미 부모가 같다면 리턴
    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1


N, M = map(int, input().split())

graph = []
parent = [i for i in range(N + 1)]  # 부모를 저장
rank = [0] * (N + 1)  # 각 노드마다 랭크를 저장
for i in range(M):
    a, b, cost = map(int, input().split())
    graph.append((a, b, cost))

graph.sort(key=lambda x: x[2])  # 마을의 비용을 오름차순으로 정렬
ans = 0  # 연결된 마을 길이의 합
end_v = 0  # 마지막에 연결된 마을 길이를 저장
for i in graph:

    if find(i[0]) != find(i[1]):
        union_(i[0], i[1])
        ans += i[2]  # 마을의 연결 비용들을 계속 더해주고
        end_v = i[2]  # 마지막에 연결된 마을 연결 비용을 저장

print(ans - end_v)  # 마지막에 연결된 연결 비용만 빼준 체 출력

'''
첫번째풀이
'''
from itertools import combinations
def solution():
    N, M = map(int, input().split())
    G = [[0 for _ in range(N+1)] for _ in range(N+1) ]

    # 도로연결 상태를 G에 갱신한다
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a][b] = c
        G[b][a] = c
    
    # 마을 2개씩 묶은 조합 담긴 배열 SET
    temp = [x for x in range(1,N+1)]
    temp = list(combinations(temp, 4))
    SET = list(combinations(temp, 2))

    # 각 마을의 집들이 연결되어 있는지 체크하고 최솟값의 유지비를 리턴하는 함수 check
    def check(houses):
        temp = []
        minSum = 0
        for one in houses:
            minVal = 1001
            for another in houses:
                if one not in temp and G[one][another] != 0:
                    if minVal > G[one][another]:
                        temp.append(one)
                        minVal = min(G[one][another], minVal)
            
            minSum += minVal
        
        return minSum
    
    answer = int(1e9)
    # 두 마을의 유지비 값의 합을 min()함수를 활용해 정답을 갱신한다.
    for townA, townB in SET:
        costA, costB = check(townA), check(townB)
        answer = min(answer, costA+costB)
    
    print(answer)
solution()


    
