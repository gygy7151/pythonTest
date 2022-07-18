'''
테트로미노
'''
'''
세번째풀이
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
#ANS의 최솟값을 0으로 수정
#만약 도형이 다 범위를 벗어나는 경우 0을리턴해줘야됨
paper =[ list(map(int, input().split())) for _ in range(N) ]

#아...도형숫자 잘못적어서 틀렸던거임.
dir = [
    [ (0,0), (0,1), (1,0), (1,1) ],
    [ (0,0), (0,1), (0,2), (0,3) ],
    [ (0,0), (1,0), (2,0), (3,0) ],
    [ (0,0), (0,1), (1,1), (2,1) ],
    [ (0,0), (0,1), (0,2), (1,0) ],
    [ (0,0), (0,1), (0,2), (1,2) ],
    [ (0,0), (1,0), (1,1), (1,2) ],
    [ (1,0), (1,1), (1,2), (0,2) ],
    [ (0,0), (1,0), (2,0), (2,1) ],
    [ (0,1), (1,1), (2,0), (2,1) ],
    [ (0,0), (0,1), (1,0), (2,0) ],
    [ (0,1), (1,0), (1,1), (1,2) ],
    [ (0,1), (1,1), (2,1), (1,0) ],
    [ (0,0), (0,1), (0,2), (1,1) ],
    [ (0,0), (1,0), (1,1), (2,0) ],
    [ (0,0), (1,0), (1,1), (2,1) ],
    [ (0,1), (1,0), (1,1), (2,0) ],
    [ (0,1), (0,2), (1,0), (1,1) ],
    [ (0,0), (0,1), (1,1), (1,2) ]
]
    

def tetromino(x,y):
    global ANS

    for i in range(19):
        result  = 0
        for j in range(4):
            try:
                nx = x + dir[i][j][0]
                ny = y + dir[i][j][1]
                result += paper[nx][ny]
            except IndexError:
                continue
            #ANS위치주의 인덱스초과나면 result 비교하면안된다
            #그리고 요소에 정수가 담겨있다고 했음. 음수도 들어갈 수 있다는 말임
            #범위벗어나는건 어차피 안더해주니깐 최댓값축에 낄수없게 예외처리됨
            ANS = max(ANS, result)

ANS = 0 
for i in range(N):
    for j in range(M):
        tetromino(i,j)

print(ANS)

'''
두번째풀이 - 10%대에서 틀림 - 그래도 틀림
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     ANS, paper = -1, [list(map(int, input().split())) for _ in range(N)]
#     dir = [
#         [ (0,0), (0,1), (1,0), (1,1) ],
#         [ (0,0), (0,1), (0,2), (0,3) ],
#         [ (0,0), (1,0), (2,0), (3,0) ],
#         [ (0,0), (0,1), (1,1), (2,1) ],
#         [ (0,0), (0,1), (0,2), (1,0) ],
#         [ (0,0), (0,1), (0,2), (1,2) ],
#         [ (0,0), (1,0), (1,1), (1,2) ],
#         [ (1,0), (1,1), (1,2), (0,2) ],
#         [ (0,0), (1,0), (2,0), (2,1) ],
#         [ (0,1), (1,1), (2,0), (2,1) ],
#         [ (0,0), (0,1), (1,0), (2,0) ],
#         [ (0,0), (0,1), (0,2), (1,1) ],
#         [ (0,1), (1,1), (2,1), (1,0) ],
#         [ (0,0), (0,1), (0,2), (1,1) ],
#         [ (0,0), (1,0), (1,1), (2,0) ],
#         [ (0,0), (1,0), (1,1), (2,1) ],
#         [ (0,1), (1,0), (1,2), (2,0) ],
#         [ (0,1), (0,2), (1,0), (1,1) ],
#         [ (0,0), (0,1), (1,1), (1,2) ]
#     ]
    
#     # x,y를 기준으로 모든 방향을 다 도는게 효율적이긴 한데 기존 구현한 코드에 논리적 오류발견
#     def tetromino(a,b,c,d):
#         nonlocal ANS
#         ax, ay, bx, by, cx, cy, dx, dy =  a[0], a[1], b[0], b[1], c[0], c[1], d[0], d[1]

#         for i in range(N):
#             for j in range(M):
#                 totalSum = 0
#                 #범위를 벗어난다고 카운트를 멈추는것이 아님
#                 #범위내에 있는 애들끼리만 다 합산해서 최댓값 비교해주어야됨
#                 #무조건 범위내에 있는애들만 더해주어야 값이 커질꺼라는 섣부른 논리적오류를 범했음.
#                 if 0  > i + ax or i + ax >= N or 0 > j + ay or j + ay >= M:
#                     continue
#                 else:
#                     totalSum += paper[i+ax][j+ay]

#                 if 0  > i + bx or i + bx >= N or 0 > j + by or j + by >= M:
#                     continue
#                 else:
#                     totalSum += paper[i+bx][j+by]

#                 if 0  > i + cx or i + cx >= N or 0 > j + cy or j + cy >= M:
#                     continue
#                 else:
#                     totalSum += paper[i+cx][j+cy]

#                 if 0  > i + dx or i + dx >= N or 0 > j + dy or j + dy >= M:
#                     continue

#                 else:
#                     totalSum += paper[i+dx][j+dy]
#                 # print(totalSum)
#                 ANS = max(ANS, totalSum)
    
#     for a, b, c, d in dir:
#         tetromino(a,b,c,d)

#     return ANS
# print(solution())



'''
첫번째풀이
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     ANS, paper = -1, [list(map(int, input().split())) for _ in range(N)]
#     dir = [
#         [ (1,0), (2,0), (3,0) ],
#         [ (0,1), (0,2), (0,3) ],
#         [ (0,1), (1,0), (1,1) ],
#         [ (1,0), (0,1), (0,2) ],
#         [ (1,0), (2,0), (2,1) ],
#         [ (-1,2), (0,1), (0,2) ],
#         [ (-2,1), (-1,1), (0,1) ],
#         [ (1,2), (0,1), (0,2) ],
#         [ (1,0), (1,1), (1,2) ],
#         [ (0,1), (1,1), (2,2) ],
#         [ (0,1), (1,0), (2,0) ],
#         [ (1,-1), (1,0), (0,1) ],
#         [ (2,1), (1,1), (1,0) ],
#         [ (2,-1), (1,-1), (1,0) ],
#         [ (1,2), (1,1), (0,1) ],
#         [ (1,-1), (1,0), (2,0) ],
#         [ (1,1), (0,1), (0,2) ],
#         [ (1,1), (1,0), (2,0) ],
#         [ (1,-1), (1,0), (1,1) ],
#     ]

#     def merge(x,y,a,b,c):
#         nonlocal ANS
#         ax, ay, bx, by, cx, cy =  a[0], a[1], b[0], b[1], c[0], c[1]
#         totalSum = paper[x][y] + paper[x+ax][y+ay] + paper[x+bx][y+by] + paper[x+cx][y+cy]
#         ANS = max(totalSum, ANS)

#     def tetromino(a,b,c):
#         ax, ay, bx, by, cx, cy =  a[0], a[1], b[0], b[1], c[0], c[1]

#         for i in range(N):
#             for j in range(M):
#                 if 0 <= i + ax < N and 0 <= j + ay < M:
#                     if 0 <= i + bx < N and 0 <= j + by < M:
#                         if 0 <= i + cx < N and 0 <= j + cy < M:
#                             merge(i,j,a,b,c)
    
#     for a, b, c in dir:
#         tetromino(a,b,c)

#     return ANS
# print(solution())ß