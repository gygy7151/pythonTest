'''
스타트와 링크 
'''
'''
세번째 접근 - 조합의 특징을 활용함
'''
# from itertools import combinations #조합 함수

# N = int(input())
# S = [list(map(int, input().split())) for _ in range(N)]
# members = [i for i in range(N)]
# possible_team = []

# #조합으로 가능한 팀 생성해주기
# for team in list(combinations(members, N//2)):
#     possible_team.append(team)

# min_stat_gap = 10000 #갭이 가장 작은 값을 찾기 위하여
# for i in range(len(possible_team)//2):
#     #A 팀
#     team = possible_team[i]
#     stat_A = 0 #A팀 능력치
#     for j in range(N//2):
#         member = team[j] #멤버
#         for k in team:
#             stat_A += S[member][k] #멤버와 함께할 경우의 능력치들
            
#     #A를 제외한 나머지 팀
#     team = possible_team[-i-1]
#     stat_B = 0
#     for j in range(N//2):
#         member = team[j]
#         for k in team:
#             stat_B += S[member][k]
            
#     min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
    
# print(min_stat_gap)


'''
두번째 접근 - 시간초과 해결
'''
# import itertools
# N = int(input())
# arr = [x for x in range(N)]
# cases = list(itertools.combinations(arr, int(N/2)))
# for i in range(N):
# 	arr[i] = list(map(int, input().split()))

# min_value = 100*N*N
# for case_a in cases:
# 	stat_A = 0
# 	stat_B = 0
# 	for x in case_a:
# 		for y in case_a:
# 			stat_A += arr[x][y]
# 	case_b = [x for x in range(N) if x not in case_a]
# 	for x in case_b:
# 		for y in case_b:
# 			stat_B += arr[x][y]
# 	min_value = min(min_value, abs(stat_A-stat_B))
# print(min_value)

from itertools import combinations
N = int(input())
members = [x for x in range(N)]
S = list(combinations(members, int(N/2)))
for i in range(N):
    members[i] = list(map(int, input().split()))
min_diff = int(1e9)
for member_a in S:
    point_a = 0
    point_b = 0
    for x in member_a:
        for y in member_a:
            point_a += members[x][y]
    member_b = [x for x in range(N) if x not in member_a]
    for x in member_b:
        for y in member_b:
            point_b += members[x][y]
    min_diff = min(min_diff, abs(point_a - point_b))
print(min_diff)


'''
첫번째 접근 - 시간초과
'''
# from itertools import combinations
# N = int(input())
# S = [ list(map(int, input().split())) for _ in range(N)]
# temp= []
# score = [0,0]
# min_diff = int(1e9)
# for i in range(N):
#     temp.append(i+1)
# teams = list(combinations(temp, int(N/2)))

# members = [i for i in range(N)]
# possible_team = []
# #조합으로 가능한 팀 생성해주기
# for teamm in list(combinations(members, N//2)):
#     possible_team.append(teamm)
# print(possible_team)
# # print(len(teams))

# def check():
#     global score
#     global min_diff
#     visited = [[False] * N for _ in range(N)]
#     for r in range(N):
#         for k in range(N):
#             if r == k:
#                 continue
#             else:
#                 if not visited[r][k]:
#                     if team[r+1] == 0 and team[k+1] == 0:
#                         score[0] += (S[r][k] + S[k][r])
#                         visited[r][k] = True
#                         visited[k][r] = True
#                     elif team[r+1] == 1 and team[k+1] == 1:
#                         score[1] += (S[r][k] + S[k][r])
#                         visited[r][k] = True
#                         visited[k][r] = True
#     diff = abs(score[0]-score[1])
#     # print(team)
#     # print(score)
#     # print(diff)
#     min_diff = min(min_diff, diff)
#     score = [0,0]

# for member in teams:
#     team = [0] * (N+1)
#     for i in member:
#         if i in member:
#             team[i] = 1
#     check()
# print(min_diff)
            


