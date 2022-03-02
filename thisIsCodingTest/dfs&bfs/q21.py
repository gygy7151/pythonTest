'''
인구이동

'''

from collections import deque
n, l, r = map(int, input().split())
popularity = [list(map(int, input().split())) for _ in range(n)]
graph = dict()
day = 0

def check(value, input, x, y):
    if l <= input <= r:
        value.append((x,y))
def border(i,j):
    value = []
    if i-1 >= 0:
        top = abs(popularity[i-1][j] - popularity[i][j])
        check(value, top, i-1, j)
                     
    if i+1 < n:
        bottom = abs(popularity[i+1][j] - popularity[i][j])
        check(value, bottom, i+1, j)

    if j-1 >= 0:
        right = abs(popularity[i][j-1] - popularity[i][j])
        check(value, right, i, j-1)

    if j+1 < n :
        left = abs(popularity[i][j+1] - popularity[i][j])
        check(value, left, i, j+1)
    if value:
        graph[(i,j)] = value

def bfs(start):
    visit = list()
    queue = deque()
    queue.append(start)
    while queue:
        enqueue = queue.popleft()
        if enqueue not in visit:
            visit.append(enqueue)
            queue.extend(graph[enqueue])
    return visit

while True:
    
    for i in range(n):
        for j in range(n):
            border(i,j)
    
    if not graph:
        break
    
    while graph:
        movement = bfs(list(graph.keys())[0])
        ppl = 0
        for move in movement:
            ppl += popularity[move[0]][move[1]]
        sum = int(ppl // len(movement))
        for move in movement:
            popularity[move[0]][move[1]] = sum
            del(graph[move])
    day += 1
    
print(day)

'''
구분선
'''
# from collections import deque
# n, l, r = map(int, input().split())
# day = 0
# popularity = [list(map(int, input().split())) for _ in range(n)]
# graph = dict()

# def check(value, input, x, y):
#     if l <= input <= r:
#         value.append((x,y))

# def border(i,j):
#     value = []
#     if i-1 >= 0:
#         top = abs(popularity[i-1][j] - popularity[i][j])
#         check(value, top, i-1, j)
        
#     if i+1 < n:
#         bottom = abs(popularity[i+1][j] - popularity[i][j])
#         check(value, bottom, i+1, j)

#     if j+1 < n:
#         right = abs(popularity[i][j-1] - popularity[i][j])
#         check(value, right, i, j+1)

#     if j-1 >= 0:
#         left = abs(popularity[i][j-1] - popularity[i][j])
#         check(value, left, i, j-1)
    
#     if value:
#         #이건그냥 (i,j)를 키로갖는 연결리스트 밸류를 연결리스트graph에 추가해주는거임
#         graph[(i,j)] = value

# def bfs(start):
#     visit = list()
#     queue = deque()
#     queue.append(start)
#     while queue:
#         enqueue = queue.popleft()
#         if enqueue not in visit:
#             visit.append(enqueue)
#             #enqueue는 (0,0)형태임
#             #graph[enqueue]  = [(),...,()]이므로
#             #append가 아닌 extend로 iterator형태로 넣어줘야됨 ()하나씩
#             queue.extend(graph[enqueue])
#     return visit


# while True:
#     for i in range(n):
#         for j in range(n):
#             border(i,j)

#     if not graph:
#         break
    
#     while graph:
#         print(graph)
#         print(graph.keys())
#         #맨첫번째꺼를 넣는다는건 맨마지막에하나남은거까지 넣기위함
#         print(list(graph.keys())[0])
#         movement = bfs(list(graph.keys())[0])
#         sum = 0
#         for move in movement:
#             sum += popularity[move[0]][move[1]]
#         result = int(sum/len(movement))
#         for move in movement:
#             popularity[move[0]][move[1]] = result
#             del(graph[move])
#     day += 1

# print(day)



'''
구분선
'''


    

# import sys 
# sys.setrecursionlimit(10**6)
# N, L, R = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# check = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# open = []

# def dfs(x,y):
#     open.append((x,y))
#     if x < 0 or y < 0 or x >= N or y >= N:
#         return
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         gap = abs(graph[x][y] - graph[nx][ny])
#         if L <= gap <= R:
#             if nx >= 0 and ny >= 0 and nx < N and ny < N:
#                 open.append((nx,ny))
#                 dfs(nx, ny)


# def numbers(_open):
#     global open
#     trimmed = set(_open)
#     new = list(trimmed)
#     num = len(new)
#     print(new)
#     total = []
#     for r in new:
#         x, y = r
#         total.append(graph[x][y])
#     people = sum(total)
#     mid = people // num
#     for r in new:
#         x, y = r
#         graph[x][y] = mid
#     open = []

#     check = True
#     for r in range(N):
#         for c in range(N):
#             for i in range(4):
#                 nx = r + dx[i]
#                 ny = c + dx[i]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     gap = abs(graph[r][c] - graph[nx][ny])
#                     if L <= gap <= R:
#                         continue
#                     else:
#                         check = False
#     if not check:
#         return False
    
#     else :
#         return True



# day = 0
# res = True
# while res:
#     for i in range(N):
#         for j in range(N):
#             dfs(i,j)
#             numbers(open)
#             if not numbers:
#                 day += 1
#             else:
#                 break    
#     print(day)