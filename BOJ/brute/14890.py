'''
경사로 - 14890
'''
from itertools import filterfalse


n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
def pos(now):
    for j in range(1, n):
        if abs(now[j] - now[j-1]) > 1:
            return False
        if now[j] < now[j-1]:
            for k in range(l):
                if j+k >= n or used[j+k] or now[j] != now[j+k]:
                    return False
                if now[j] == now[j+k]:
                    used[j+k] = True
        elif now[j] > now[j-1]:
            for k in range(l):
                if j-k-1 < 0 or used[j-k-1] or now[j-1] != now[j-k-1]:
                    return False
                if now[j-1] == now[j-k-1]:
                    used[j-k-1] = True
    return True



#가로확인
for i in range(n):
    used = [False for _ in range(n)]
    if pos(graph[i]):
        result += 1

for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):
        result += 1

print(result)