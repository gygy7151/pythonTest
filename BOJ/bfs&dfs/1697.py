'''
숨바꼭질1697
'''
# n, k = map(int, input().split())
# visited = [0 for _ in range(100001)]
# def bfs(start):
#     q = [start] 
#     visited[start] = 1 <--이거하면안됨
#     while q:
#         d = q.pop(0)
#         if d == k:
#             return visited[d]
#         for n in [d-1, d+1, 2*d]:
#             if 1 <= n <= 100000 and not visited[n]:
#                 visited[n] = visited[d] + 1
#                 q.append(n)
# print(bfs(n))

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
def bfs(s):
    q = [s]
    while q:
        v = q.pop(0)
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

print(bfs(n))

