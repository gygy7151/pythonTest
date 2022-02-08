'''
여행계획 - MST서로소집합자료구조
'''
v, e = map(int, input().split())
graph = [] * (v+1)
#parent = [] * (v+1)하면안됨!! [,,,...,] len(parent) = 1이되는 리스트하나만 존재하게됨 
parent = [[] for _ in range(v+1)]


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

for i in range(0, v+1):
    parent[i] = i
    
for i in range(1, v+1):
    edges = list(map(int, input().split()))
    for j, edge in enumerate(edges):
        if edge == 1:
            union_parent(parent, i, j+1)

wishes = list(map(int, input().split()))
start = wishes[0]

def solution():    
    for wish in wishes[1:len(wishes)]:
        if find_parent(parent, start) != find_parent(parent, wish):
            return False
        else:
            return True

answer = solution()
if answer:
    print('YES')

else:
    print('NO')



