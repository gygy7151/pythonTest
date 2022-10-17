'''
치킨배달
'''
# 집 위치를 먼저 담은 배열 house
# M개는 조합을 이용하고
# 치킨집 위치 정보를 담은 배열 city
from itertools import combinations
def solution():
    N, M = map(int, input().split())
    houses = []
    chickens = []

    for i in range(N):
        data = list(map(int, input().split()))
        
        for j in range(N):
            if data[j] == 1: # 집
                houses.append((i,j))
            
            elif data[j] == 2: #치킨집
                chickens.append((i,j))

    min_city_chicken_dis = int(1e9)
    for set in list(combinations(chickens, M)):
    # 집마다 모든 치킨집별로 치킨 거리를 구해 그중 제일 작은 치킨거리를 result에 담는다.
        city_chicken_dis = 0
        
        for house in houses:
            r1, c1 = house
            chicken_dis = int(1e9)
            
            for r2, c2 in set:
                dis = abs(r1-r2) + abs(c1-c2)
                chicken_dis = min(chicken_dis, dis)
            
            city_chicken_dis += chicken_dis

        min_city_chicken_dis = min(city_chicken_dis, min_city_chicken_dis)
    
    print(min_city_chicken_dis)
solution()










# house 총합 중 최솟값을 구한 뒤 출력한다.
# 엇 근데 치킨집 중 최대 M개를 고르고 나머지는 모두 폐업시켜야 한다네..
