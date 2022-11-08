'''
욕심쟁이판다
'''
'''
첫번째풀이
'''
import sys
N = int(input())

order = [] # 대나무 양과 좌표 담는 배열 order
forest = [] # 나무 상태 값 정보를 담은 2차원 배열 forest

for i in range(N):
    row = [ int(x) for x in input().split()]
    for j in range(N):
        order.append([row[j],j,i]) #대나무 양, x,y
    
    forest.append(row)

#내림차순 정렬(대나무 양 기준)
order.sort(reverse=True)

answer = 0
maxDays = [[1 for _ in range(N)] for _ in range(N)]
for t in order:
    tree, x, y = t
    
    tmp = []
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if forest[y][x] < forest[ny][nx]:
                tmp.append((maxDays[ny][nx]))
        

    if len(tmp) != 0:
        maxDays[y][x] = max(tmp) + 1
    
    if answer < maxDays[y][x]:
        answer = maxDays[y][x]

print(answer)

