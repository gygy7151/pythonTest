'''
RGB 거리2
'''
'''
두번째풀이
'''
# 0:빨강 1:초록 2:파랑
def dfs(h_color, h_num):
    print('dfs돌았당')
    global answer
    global house_colors
    answer[h_num] = min(cost[h_num][h_color], answer[h_num])
    house_colors[h_num] = h_color
    if house_colors[1] != house_colors[0] and house_colors[N-1] != house_colors[0]:
        if house_colors[N-2] != house_colors[N-1] and house_colors[0] != house_colors[N-1]:
            if h_num % N != h_num % N and h_num % N != (h_num-1) % N:
                for next_h_color in [0,1,2]:
                    if next_h_color != h_color:
                        print('안걸림?')
                        dfs(next_h_color, h_num+1)
N = int(input())
INF = int(1e9)
house_colors = [-1] * N
answer = [INF] * N
cost = [list(map(int, input().split())) for _ in range(N)]
for i in range(3):
    dfs(i, 0)
print(answer)
answer = sum(answer)
print(answer)



'''
첫번째풀이 - 틀림
'''
# # 0:빨강 1:초록 2:파랑
# def dfs(h_color, h_num):
#     print('dfs돌았당')
#     global answer
#     global house_colors
#     answer[h_num] = min(cost[h_num][h_color], answer[h_num])
#     house_colors[h_num] = h_color
#     if house_colors[1] != house_colors[0] and house_colors[N-1] != house_colors[0]:
#         if house_colors[N-2] != house_colors[N-1] and house_colors[0] != house_colors[N-1]:
#             if h_num % N != h_num % N and h_num % N != (h_num-1) % N:
#                 for next_h_color in [0,1,2]:
#                     if next_h_color != h_color:
#                         print('안걸림?')
#                         dfs(next_h_color, h_num+1)
# N = int(input())
# INF = int(1e9)
# house_colors = [-1] * N
# answer = [INF] * N
# cost = [list(map(int, input().split())) for _ in range(N)]
# for i in range(3):
#     dfs(i, 0)
# print(answer)
# answer = sum(answer)
# print(answer)


