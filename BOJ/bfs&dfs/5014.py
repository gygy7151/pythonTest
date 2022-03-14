'''
숨바꼭질5014
'''
F, S, G, U, D = map(int, input().split())
visited = [-1] * (F+1)
def bfs(s):
    q = []
    q.append(s)
    visited[s] = 0
    while q:
        f = q.pop(0)
        if f == G:
            return
        for n in (f+U, f-D):
            if n <= 0 or n > F:
                continue
            else:
                if visited[n] == -1:
                    visited[n] = visited[f] + 1
                    q.append(n)
bfs(S)
if S == G:
    print(0)
elif visited[G] == -1:
    print('use the stairs')
else:
    print(visited[G])