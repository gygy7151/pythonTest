'''
빙산 - 2573번
'''
from collections import deque
from sys import stdin


def count_ice():
    # TODO: 빙산이 2개 이상의 덩어리로 분리되었는지 검사
    visited = [[False for _ in range(M)] for _ in range(N)]
    que = deque()
    check = False  # 1 덩어리 있으면 True
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 and not visited[i][j]:
                if check:  # 기존 덩어리말고 다른 덩어리 발견
                    return True
                visited[i][j] = True
                que.append([i, j])
                while que:
                    cx, cy = que.popleft()
                    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                        nx, ny = cx + dx, cy + dy
                        if not 0 <= nx < N or not 0 <= ny < M or visited[nx][ny] or ice[nx][ny] == 0:
                            continue
                        visited[nx][ny] = True
                        que.append([nx, ny])
                check = True
    return False


def melt_ice():
    # TODO: 빙하를 녹임
    print('녹는다')
    update = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] == 0:
                continue
            for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                nx, ny = i + dx, j + dy
                if not 0 <= nx < N or not 0 <= ny < M or ice[nx][ny] != 0:
                    continue
                update[i][j] += 1
    for i in range(N):
        for j in range(M):
            if ice[i][j] == 0:
                continue
            ice[i][j] -= update[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0
    for i in range(N):
        print(ice[i])
    


def check_ice():
    # TODO: 빙하가 존재하는지 검사
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                return True
    return False


N, M = map(int, stdin.readline().split())
ice = list(list(map(int, stdin.readline().split())) for _ in range(N))
year = 0
while not count_ice():
    if not check_ice():
        year = 0
        break
    year += 1
    melt_ice()
print(year)