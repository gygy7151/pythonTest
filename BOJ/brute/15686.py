'''
치킨배달 - 15686번
'''
from itertools import combinations
def chi_count(temp,house,store):
    # 각 집의 최소 치킨거리 구하기
    for h in house:
        hy, hx = h
        for s in store:
            sy, sx = s
            dis = abs(hy-sy) + abs(hx-sx)
            temp[hy][hx] = min(dis, temp[hy][hx])
    # 도시의 치킨거리 구하기
    res = 0
    for h in house:
        hy, hx = h
        res += temp[hy][hx]
    return res
    
n, m = map(int, input().split())
house = []
store = []
temp_store = []
for y in range(n):
    graph = list(map(int, input().split()))
    for x, el in enumerate(graph):
        if el == 1:
            house.append([y,x])
        elif el == 2:
            store.append([y,x])
pairs = list(combinations(store, m))
answer = int(1e9)
# m개 치킨집 조합
for m_store in pairs:
    # print('시작')
    temp = [[int(1e9)]*n for _ in range(n)]
    # 치킨거리 구하기
    res = chi_count(temp,house,m_store)
    answer = min(res, answer)
    # print('끝')
print(answer)