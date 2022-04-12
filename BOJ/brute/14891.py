'''
톱니바퀴 - 14891
'''
'''
두번째 코드 - 이번엔 회전으로 톱니바퀴 정보를 기준으로 좌우로 인접한 톱니바퀴를 재귀함수 형식으로 접근했다.
'''
circles = []
for i in range(4):
    circles.append(list(map(int, input().rstrip())))

def rotation(num, dir, side):
    global circles
    if 0 <= (num+side) < 4:
        if side == 1:
            if circles[num][2] != circles[num+side][6]:
                rotation(num+side, -dir, side)
                handle_rotation(num+side, -dir)
        else:
            if circles[num][6] != circles[num+side][2]:
                rotation(num+side, -dir, side)
                handle_rotation(num+side, -dir)
def handle_rotation(num, dir):
    if dir == 1:
        circles[num].insert(0, circles[num].pop())
    else:
        circles[num].append(circles[num][0])
        del circles[num][0]
k = int(input())
datas = []
score = 0
for _ in range(k):
    num, rot = map(int, input().split())
    rotation(num-1, rot, 1)
    rotation(num-1, rot, -1)
    handle_rotation(num-1, rot)

for d in range(4):
    if circles[d][0] == 1:
        if d == 0:
            score += 1
        elif d == 1:
            score += 2
        elif d == 2:
            score += 4
        elif d == 3:
            score += 8
print(score)






'''
첫번째 코드 - 인덱스범위초과까진 잘 해결 되었는데..주어진 톱니바퀴 기준이 아닌 1번부터 순서대로 회전을 핸들링하니 결과가 틀리게 나왔다.
'''
# circles = [ [x for x in input()] for _ in range(4) ]
# for i in range(4):
#     print(circles[i])
# datas = []
# k = int(input())
# for _ in range(k):
#     a, b = map(int, input().split())
#     datas.append((a, b))
# def rotate(d,i):
#     if d == 1:
#         circles[i] = [circles[i][7], circles[i][0], circles[i][1], circles[i][2], circles[i][3], circles[i][4], circles[i][5], circles[i][6]]
#         circles[i+1] = [circles[i+1][1], circles[i+1][2], circles[i+1][3], circles[i+1][4], circles[i+1][5], circles[i+1][6], circles[i+1][7], circles[i+1][0]]
#     elif d == -1:
#             circles[i+1] = [circles[i+1][7], circles[i+1][0], circles[i+1][1], circles[i+1][2], circles[i+1][3], circles[i+1][4], circles[i+1][5], circles[i+1][6]]
#             circles[i] = [circles[i][1], circles[i][2], circles[i][3], circles[i][4], circles[i][5], circles[i][6], circles[i][7], circles[i][0]]
# while datas:
#     print('시작')
#     turn = [False] * 5
#     num, d = datas.pop(0)
#     print("{} num이다".format(num))
#     turn[num] = True
#     for r in range(1,5):
#         # 왼쪽
#         if r < num and 0 < r and r+1 <= 3:
#             if turn[r+1] and circles[r][2] != circles[r+1][6]:
#                 turn[r] = True
#                 rotate(-d,r)
#         # 오른쪽
#         elif r > num and r <= 3:
#             if turn[r-1] and circles[r][6] != circles[r-1][2]:
#                 turn[r] = True
#                 rotate(-d,r)
# for i in range(4):
#     print(circles[i])

# score = 0
# for i in range(4):
#     if circles[i][0] == '1':
#         if i == 0:
#             score += 1
#         elif i == 1:
#             score += 2

#         elif i == 2:
#             score += 4
    
#         elif i == 3:
#             score += 8
# print(score)
    
'''
첫번째 바퀴회전 코드
'''
    # for i in range(3):
    #     if circles[i][2] == circles[i+1][6]:
    #         continue
    #     if d == 1:
    #         circles[i] = [circles[i][7], circles[i][0], circles[i][1], circles[i][2], circles[i][3], circles[i][4], circles[i][5], circles[i][6]]
    #         circles[i+1] = [circles[i+1][1], circles[i+1][2], circles[i+1][3], circles[i+1][4], circles[i+1][5], circles[i+1][6], circles[i+1][7], circles[i+1][0]]
    #     elif d == -1:
    #         circles[i+1] = [circles[i+1][7], circles[i+1][0], circles[i+1][1], circles[i+1][2], circles[i+1][3], circles[i+1][4], circles[i+1][5], circles[i+1][6]]
    #         circles[i] = [circles[i][1], circles[i][2], circles[i][3], circles[i][4], circles[i][5], circles[i][6], circles[i][7], circles[i][0]]
    #     print(circles[i][2],circles[i+1][6])
