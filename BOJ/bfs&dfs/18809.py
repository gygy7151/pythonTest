'''
Gaaaaaaaaaarden - 이건 걍 외워야겠다.
'''
'''
두번째풀이 - 꽃이 필때 꽃을 바로 세는걸로 바꿔 접근했더니 시간초과해결했다고 함 - 추후 다시 시도..
참조 : https://regularmember.tistory.com/189
'''
from collections import deque
ans = 0
N, M, G, R = list(map(int, input().split()))
brownSoilSize = 0
map = [[ 0 for _ in range(50)] for _ in range(50)]
gtime = [[ 0 for _ in range(50)] for _ in range(50)] # 초록색 배양액이 퍼진 시간을 저장
rtime = [[ 0 for _ in range(50)] for _ in range(50)] # 빨간색 배양액이 퍼진 시간을 저장
flower = [[ 0 for _ in range(50)] for _ in range(50)] # 꽃이 피었는지 체크

dir = [(0,1), (0,-1), (1,0), (-1,0)]

brownSoil = [] # 배양액을 뿌릴 수 있는 땅의 좌표를 저장
green = [] # 초록색 배양액을 뿌릴 좌표를 저장
red = [] # 빨간색 배양액을 뿌릴 좌표를 저장

# def bfs():
#     gq = 
#     rq = deque()


'''
첫번째풀이 - 틀림
'''
'''
정원은 땅과 호수로 이루어져있고
2차원 격자판 모양이다
인건비 절감을 위해 초록색 배양액과 빨간색 배양액을 땅에 뿌려 꽃을 피울것이다
배양액은 매초마다 이전에 배양액이 도달한 적 없는 인접한 땅으로 퍼져가다

하얀색칸은 배양액을 뿌릴 수 없는땅
황토색칸은 배양액을 뿌릴 수 있는땅
하늘색은 호수 ->  뿌릴 수 없는땅

초록색 배양액과 빨간색 배양액이 동일한 시간에 

'''

# 배양액을 뿌릴 수 있는 땅의 정보 graph (0:호수, 1:배양액 뿌릴수 없는땅, 2:배양액 뿌릴 수 있는땅)
# from itertools import combinations
# from collections import deque
# import sys
# import copy
# input = sys.stdin.readline

# def solution():
#     #1 [] garden에 배양액을 뿌릴 수 있는 곳에 빨간색, 초록색 배양액을 뿌려준다. 이때 부분집합 활용
#     #2 [] 모든 배양액이 사용되었다면, 배양액이 뿌려진 좌표로부터 배양액을 퍼뜨려보자
#     N, M, G, R = map(int, input().split())
#     maps = [list(map(int, input().split())) for _ in range(N)]
#     answer = -1

#     def bfs(copy_map, total, green):
#         cnt  = 0
#         green_q = deque()
#         red_q = deque()
        
        
#         for r, c in total:
#             for r,c in list(total & green):
#                 green_q.append((r,c))
#                 copy_map[r][c] = 3 # 초록색배양액
#             for r, c in list(total - green):
#                 red_q.append((r,c))
#                 copy_map[r][c] = 4 # 빨강색배양액
        
#         while green_q:
#             g_temp = set()
#             r_temp = set()

#             while green_q:
#                 x, y = green_q.popleft()
#                 copy_map[x][y] = 3

#                 if 0 <= y + 1 < M:
#                     if copy_map[x][y+1] == 1 or copy_map[x][y+1] == 2:
#                         g_temp.add((x,y+1))

#                 if 0 <= y - 1 < M:
#                     if copy_map[x][y-1] == 1 or copy_map[x][y-1] == 2:
#                         g_temp.add((x,y-1))
                
#                 if 0 <= x + 1 < N:
#                     if copy_map[x+1][y] == 1 or copy_map[x+1][y] == 2:
#                         g_temp.add((x+1,y))

#                 if 0 <= x - 1 < N:
#                     if copy_map[x-1][y] == 1 or copy_map[x-1][y] == 2:
#                         g_temp.add((x-1,y))

            
#             while red_q:
#                 x, y = red_q.popleft()
#                 copy_map[x][y] = 4
#                 if 0 <= y + 1 < M:
#                     if copy_map[x][y+1] == 1 or copy_map[x][y+1] == 2:
#                         r_temp.add((x,y+1))

#                 if 0 <= y - 1 < M:
#                     if copy_map[x][y-1] == 1 or copy_map[x][y-1] == 2:
#                         r_temp.add((x,y-1))
                
#                 if 0 <= x + 1 < N:
#                     if copy_map[x+1][y] == 1 or copy_map[x+1][y] == 2:
#                         r_temp.add((x+1,y))

#                 if 0 <= x - 1 < N:
#                     if copy_map[x-1][y] == 1 or copy_map[x-1][y] == 2:
#                         r_temp.add((x-1,y))

            
#             inter = g_temp & r_temp
#             g_temp = g_temp - inter
#             r_temp = r_temp - inter

#             for r,c in inter:
#                 copy_map[r][c]= 5
#                 cnt += 1
            
#             for r, c in g_temp:
#                 copy_map[r][c] = 3
            
#             for r, c in r_temp:
#                 copy_map[r][c] = 4

#             green_q.extend(g_temp)
#             red_q.extend(r_temp)

#         return cnt

#     location = []

#     for i in range(N):
#         for j in range(M):
#             if maps[i][j] == 2:
#                 location.append((i,j))

#     for total in combinations(location, G + R):
#         for green in combinations(total, G):
#             copy_maps = copy.deepcopy(maps)
#             answer = max(answer, bfs(copy_maps, set(total), set(green)))
    
#     return answer

# print(solution())







#     #3 [] #1,2 과정을 거친 후 시간에 따라 배양액이 퍼지는 과정을 시뮬레이션 한다
#     #4 [] #1~3 과정을 모든 경우의 수에 대해 적용해보고 피울 수 있는 꽃의 최대 개수를 출력한다




