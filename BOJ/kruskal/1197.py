'''
최소스패닝트리
'''
'''
두번째풀이 - 크루스칼알고리즘
'''
import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))
 
Elist.sort(key=lambda x: x[2])
 
 
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
 
answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)
'''
첫번째풀이 - 메모리초과
'''
# import sys
# input = sys.stdin.readline

# def dfs(vertex, cost, depth):
#     global ans
#     if depth == V:
#         ans = min(ans, cost)
#         return
#     for index, node in enumerate(graph[vertex]):
#         if node != 'inf':
#             dfs(index, cost+graph[vertex][index], depth+1)

# V, E = map(int, input().split())
# graph = [['inf'] * (V+1) for _ in range(V+1)]
# for _ in range(E):
#     A, B, cost = map(int, input().split())
#     graph[A][B] = cost
# ans = 2147483700
# for i in range(1, V+1):
#     dfs(i, 0, 1)
# print(ans)