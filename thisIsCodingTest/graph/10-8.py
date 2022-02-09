'''
어두운 길- 크루스칼알고리즘활용
n개의 집과 m개의 도로
집은 0번부터 n-1번까지
가로등을하루동안켜기위한 비용 = 해당도로의길이
정부에선 임의의 두집에 대하여 가로등이 켜진도로만
오갈수있도록하고, 일부가로등을 비활성화하고싶다.
일부가로등을 비활성화해야 절약할 수 있는 최대금액 출력프로그램
싸이클이존재하지않음
'''
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
edges= []
parent= [0] * (v)
result = 0

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

for i in range(v):
    parent[i] = i

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    
    else:
        result += cost

print(result)