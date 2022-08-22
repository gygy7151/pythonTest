'''
감시 - dfs
'''
# import copy
# INF = int(1e9)

# # 동 서 남 북
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
#              [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

# def watch(y, x, direction, tmp):
#     for d in direction:
#         nx = x
#         ny = y
#         while True:
#             # nx += dx[d]
#             # ny += dy[d]
#             # print(nx)
#             # print(ny)
#             # print('-----')
#             if nx >= 0 and nx < m and ny >= 0 and ny < n and tmp[ny][nx] != 6:
#                 if tmp[ny][nx] == 0:
#                     tmp[ny][nx] = '#'
#                     # for i in range(n):
#                     #     print(tmp[i])
#             else:
#                 break

# def dfs(office, cnt):
#     global ans
#     tmp = copy.deepcopy(office)
#     if cnt == cctv_cnt:
#         c = 0
#         for i in tmp:
#             c += i.count(0)
#         ans = min(ans, c)
#         return
#     y, x, cctv = q[cnt]
#     for i in direction[cctv]:
#         watch(y, x, i, tmp)
#         dfs(tmp, cnt + 1)
#         tmp = copy.deepcopy(office)

# n, m = map(int, input().split())
# office = []
# cctv_cnt = 0
# q = []
# ans = INF
# for i in range(n):
#     input_data = list(map(int, input().split()))
#     office.append(input_data)
#     for j in range(len(input_data)):
#         if input_data[j] != 0 and input_data[j] != 6:
#             cctv_cnt += 1
#             q.append([i, j, input_data[j]])

# dfs(office, 0)
# print(ans)


'''
district -> 안됨..pypy로품
'''
import copy
dir = ((-1,0), (1,0), (0, -1), (0,1))
direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [2, 1], [1, 3], [3, 0]],
    [[0, 2, 1], [2, 1, 3], [1, 3, 0], [3, 0, 2]],
    [[0, 1, 2, 3]]
]
def watch(x,y, direction, tmp):
    for d in direction:
        nx = x
        ny = y
        while True:
            nx += dir[d][0]
            ny += dir[d][1]
            # print(nx)
            # print(ny)
            # print('-----')
            if 0 <= nx < m and  0 <= ny < n and tmp[ny][nx] != 6:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
            else:
                # if 0 <= nx < m and  0 <= ny < n and 1 <= tmp[ny][nx] <= 5:
                #     continue -> 이거 하면 안된다.. 중복되기 때문에 카운트가 중복됨
                break

def dfs(office, cnt):
    global ans
    tmp = copy.deepcopy(office)
    #0부터 시작하기 때문에 추가로 +1 안해줘도됨
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    x, y, cctv = q[cnt]
    for i in direction[cctv]:
        watch(x, y, i, tmp)
        dfs(tmp, cnt + 1) #여기서 cnt는 q리스트에 접근하는 인덱스임
        tmp = copy.deepcopy(office)


n, m  = map(int, input().split())
office = []
cctv_cnt = 0
q = []
ans = int(1e9)
for i in range(n): #y 가로
    input_data = list(map(int, input().split()))
    office.append(input_data)
    for j in range(len(input_data)): #x 세로
        if input_data[j] != 0 and input_data[j] != 6:
            cctv_cnt += 1
            q.append([j, i, input_data[j]])

dfs(office, 0)
print(ans)