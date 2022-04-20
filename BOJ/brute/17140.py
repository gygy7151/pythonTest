'''
이차원배열과연산 - 시간도 줄이고, 코드길이와 메모리도 줄였다
'''
from collections import Counter
def transpose(maps):
    next_maps = []
    max_col = 0
    for row in maps:
        next_row = []
        temp = sorted(list(Counter(row).items()), key = lambda x : (x[1], x[0]))
        for num, cnt in temp:
            if num == 0:
                continue
            next_row.append(num)
            next_row.append(cnt)
        max_col = max(max_col, len(next_row))
        next_maps.append(next_row)
    # 0개수 채우기
    for row in next_maps:
        if len(row) < max_col:
            for _ in range(max_col - len(row)):
                row.append(0)
    return next_maps
r, c, k = map(int, input().split())
maps = []
for _ in range(3):
    maps.append(list(map(int, input().split())))
    time = 0
    find = False
while time <= 100:
    if r <= len(maps) and c <= len(maps[0]) and maps[r-1][c-1] == k:
        print(time)
        find = True
        break
    time += 1
    if len(maps) >= len(maps[0]):
        next_maps = transpose(maps)
        maps = next_maps
        continue

    elif len(maps) < len(maps[0]):
        maps = list(map(list, zip(*maps)))
        next_maps = transpose(maps)
        next_maps = list(map(list, zip(*next_maps)))
        maps = next_maps

if not find:
    print('-1')
