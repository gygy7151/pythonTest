'''
어항정리
'''
'''
정답
'''
def stackBowl1(fishes, N):
    '''
    2. 어항 쌓기
    가장 왼쪽에 있는 어항을 그 오른쪽 어항 위에 올려 놓음
        2개 이상 쌓인 어항, 90도 시계방향 회전, 바닥 왼쪽 어항위에 공중부양된 어항 중
        가장 왼쪽에 있는 어항 존재

        위 2 번 과정을 공중부양 시킨 어항 중
        가장 오른쪽에 있는 어항의 아래 바닥에 있는 어항이 있을 때 까지
    '''

    # 처음 회전 부분
    bowl = fishes[:]
    rot = [[bowl[0]], [bowl[1]]]

    # 앞에서 부터 h 만큼 잘라내기
    bowl = bowl[2:]

    # 첫번째 회전 이후
    while True:
        h = len(rot) # 높이
        w = len(rot[0]) # 밑변
        # 남은 길이 - 높이 >= 0
        if len(bowl) - h >= 0:
            # 회전 == 떼어내서 회전 >
            # 회전 배열 배열 > 밑변 높이 바뀜
            temp = [[0] * h for _ in range(w)]
            for i in range(0, w):
                for j in range(h):
                    temp[i][j] = rot[h - 1 - j][i]
            # 밑에 넣기
            rot = temp + [bowl[:h]]
            # 앞에서 부터 h 만큼 잘라내기
            bowl = bowl[h:]
        else:
            rot[-1] = rot[-1] + bowl
            break

    # 사각 행렬 만들게 -1 붙임 # 불가능한 곳
    for i in range(len(rot)-1):
        rot[i].extend([-1] * (len(rot[-1])-len(rot[i])))
    '''
     d = (모든 인접한 두 어항 차이) // 5
        d > 0:
        두 어항 중 물고기 많은 곳에 있는 d마리 물고기 > 적은곳
        이 과정 모든 인접한 칸에 대해 동시 발생
    '''
    r = len(rot)
    c = len(rot[-1])
    temp = [[0]*c for _ in range(r)]
    for x in range(len(rot)):
        for y in range(len(rot[x])):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= len(rot) or ny < 0 or ny >= len(rot[x]):
                    continue
                if rot[nx][ny] == -1:
                    continue
                d = (rot[x][y] - rot[nx][ny])// 5
                if d > 0:
                    if rot[x][y] < rot[nx][ny]:
                        temp[x][y] += d
                        temp[nx][ny] -= d
                    elif rot[nx][ny] < rot[x][y]:

                        temp[nx][ny] += d
                        temp[x][y] -= d

    for i in range(r):
        for j in range(c):
            if rot[i][j] != -1:
                rot[i][j] += temp[i][j]

    # 한 줄로 만들기
    '''
        어항 다시 일렬로
        가장 왼쪽에 있는 어항부터, 가장 아래쪽에 있는 어항 순
        '''
    #r = len(temp[0])
    cnt = 0
    bowl = []

    for c in range(len(rot[0])):
        for r in range(len(rot)-1, -1, -1):
           #값을 변경했을 때만
           if rot[r][c] != -1:
               bowl.append(rot[r][c])

    fishes = bowl[:]
    return fishes
def stackBowl2(fishes, N):
    """
    가운데를 중심으로  N/2개를 공중 부양시켜 전체를 시계 방향으로 180도 회전 시킨 다음, 오른쪽 N/2개
    두 번 반복
    두 번 반복 하면 바닥에 있는 어항의 수는 N/4개
    """
    left = list(reversed(fishes[:(N//2)]))
    right = fishes[N//2:]
    stackbowl = [left] + [right]

    left = [[0]*(N//4) for _ in range(2)]
    right = [[0]*(N//4) for _ in range(2)]
    for i in range(2):
        for j in range(N//2):
            if j < N//4:
                left[i][j] = stackbowl[i][j]
            else:
                right[i][j-(N//4)] = stackbowl[i][j]
    # left만 180도 회전
    left = list(reversed(left))
    leftup = list(reversed(left[0]))
    leftdown = list(reversed(left[1]))
    left =  [leftup] + [leftdown]
    stackbowl = left + right

    r = 4
    c = N//4
    temp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                d = (stackbowl[x][y] - stackbowl[nx][ny])// 5
                if d > 0:
                    if stackbowl[x][y] < stackbowl[nx][ny]:
                        temp[x][y] += d
                        temp[nx][ny] -= d
                    elif stackbowl[nx][ny] < stackbowl[x][y]:
                        temp[nx][ny] += d
                        temp[x][y] -= d

    for x in range(r):
        for y in range(c):
            stackbowl[x][y]+= temp[x][y]
    bowl = []
    for c in range(N//4):
        for r in range(3, -1, -1):
            bowl.append(stackbowl[r][c])
    fishes = bowl[:]
    return fishes

def fillFish(fishes, N):
    # 물고기 수 가장 적은 어항에 물고기 한마리 넣음
    # if 여러개 >
    #  모두 1마리 넣음
    minCnt = min(fishes)
    for i in range(N):
        if fishes[i] == minCnt:
            fishes[i] += 1
    return fishes
def solve(fishes, N):
    fishes = fillFish(fishes, N)
    fishes = stackBowl1(fishes, N)
    fishes = stackBowl2(fishes, N)

    """ 
    물고기가 가장 많이 들어있는 어항과 가장 적게 들어있는 어항의 물고기 수 차이가 K 이하가 되려면 
    어항을 몇 번 정리해야하는지 구해보자.
    """
    return fishes
if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N, K = map(int, input().split())
    fishes = list(map(int, input().split()))
    op = 0
    while max(fishes) - min(fishes) > K:
        op += 1
        fishes = solve(fishes, N)
    print(op)
# #물고기한마리넣기
# def fillFish(fishes, N):
#     '''
#     1. 물고기수 가장 적은 어항에 물고기 한마리 넣음
#     2. 가장 적은 어항이 여러개면 모두 한마리씩 넣음
#     '''
#     minCnt = min(fishes)
#     for i in range(N):
#         if fishes[i] == minCnt:
#             fishes[i] += 1
#     return fishes
# #어항쌓기
# def stackBowl1(fishes, N):
#     '''
#     1.가장 왼쪽에 있는 어항을 그 오른쪽 어항위에 올려 놓음
#     '''
#     #처음 회전부분
#     bowl = fishes[:]
#     rot = [[bowl[0]], [bowl[1]]]

#     #앞에서 부터 h만큼 잘라내기
#     bowl = bowl[2:]

#     #첫번째 회전 이후
#     while True:
#         h = len(rot) #높이
#         w = len(rot[0]) #밑변
#         # 남은 길이 - 높이 >= 0
#         if len(bowl) - h >= 0:
#             #회전 == 떼어내서 회전 >
#             #회전배열배열 > 밑변높이바뀜
#             temp = [[0] *  h for _ in range(w)]
#             for i in range(0,w):
#                 for j in range(h):
#                     temp[i][j] = rot[h-1-j][i]
#             #밑에 넣기
#             rot = temp + [bowl[:h]]

#             #앞에서 부터 h만큼 잘라내기
#             bowl = bowl[h:]
#         else:
#             #결국 이어붙여주게되어있음 호오..아름답다
#             rot[-1] = rot[-1] + bowl
#             break
#     #물고기수 조절위한 사전작업
#     #사각행렬 만들기 위해 높이가 다른 곳은 -1을 붙임
#     for i in range(len(rot)-1):
#         rot[i].extend([-1] * (len(rot[-1]) - len(rot[i])))
    
#     #물고기수조절
#     '''
#      1. 모든 인접한 두 어항에 대해 물고기 수 차이를 구함
#      2. 이 차이를 5로 나눈 몫 d
#      3. if d > 0:
#       3-1. 두 어항 중 물고기가 많은 곳에 - d마리해주고
#       3-2. 물고기가 적은 곳에 + d 마리 해준다
#       3-3. 위 과정은 모든 인접한 칸에 동시 발생
#       3-4. 주의) 사각행렬을 위해 -1로 채워진 곳은 예외처리필수
#       3-5. 동시발생한 바뀐내용을 temp에 담고 본래 rot에 다시 더해준다
#     '''
#     r = len(rot) #y 행개수
#     c = len(rot[-1]) #x 렬개수
#     temp = [[0] * c for _ in range(r)]
#     for x in range(r):
#         for y in range(len(rot[x])):
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if nx < 0 or nx >= r or ny < 0 or ny >= len(rot[x]):
#                     continue
#                 # 3-4 관련코드
#                 if rot[nx][ny] == -1:
#                     continue
#                 #여긴 방향 d가 아님 오해노노
#                 d = (rot[x][y] - rot[nx][ny]) // 5
#                 if d > 0:
#                     if rot[x][y] < rot[nx][ny]:
#                         temp[x][y] += d
#                         temp[nx][ny] -= d
#                     elif rot[nx][ny] < rot[x][y]:
#                         temp[nx][ny] += d
#     # 3-5 관련코드
#     for i in range(r):
#         for j in range(c):
#             if rot[i][j] != -1:
#                 rot[i][j] += temp[i][j]
#     #어항 일렬정렬
#     '''
#     1. 가장 왼쪽 에서부터
#     2. 맨아래부터 맨위로 차례대로 
#     => 열마다 접근해 정렬
#     '''
#     cnt = 0
#     bowl = []
#     for c in range(len(rot[0])):
#         for r in range(len(rot)-1, -1, -1):
#             #c는 열 r은 행
#             #값을 변경했을때만
#             if rot[r][c] != -1:
#                 bowl.append(rot[r][c])
#     fishes = bowl[:]
#     return fishes

# def stackBowl2(fishes, N):
#     #N//2개, N//4개 공중부양
#     left = list(reversed(fishes[:(N//2)]))
#     right = fishes[N//2:]
#     stackbowl = [left] +  [right]

#     left = [[0]*(N//4) for _ in range(2)]
#     right = [[0]*(N//4) for _ in range(2)]

#     for i in range(2):
#         for j in range(N//2):
#             if j < N //4:
#                 left[i][j] = stackbowl[i][j]
#             else:
#                 right[i][j-(N//4)] = stackbowl[i][j]
#     #left만 180도 회전
#     left = list(reversed(left))
#     leftup = list(reversed(left[0]))
#     leftdown = list(reversed(left[1]))
#     left = [leftup] + [leftdown]
#     stackbowl = left + right

#     #다시또 물고기수 조절
#     r = 4
#     c = N//4
#     temp = [[0] * c for _ in range(r)]
#     for x in range(r):
#         for y in range(c):
#             for i in range(4):
#                 nx, ny = x + dx[i], y + dy[i]
#                 if nx < 0 or nx >= r or ny < 0 or ny >= c:
#                     continue
#                 d = (stackbowl[x][y] - stackbowl[nx][ny])//5
#                 if d > 0:
#                     if stackbowl[x][y] < stackbowl[nx][ny]:
#                         temp[x][y] += d
#                         temp[nx][ny] -= d
#                     elif stackbowl[nx][ny] < stackbowl[x][y]:
#                         temp[nx][ny] += d
#                         temp[x][y] -= d
#     for x in range(r):
#         for y in range(c):
#             stackbowl[x][y] += temp[x][y]
#     bowl = []
#     for c in range(N//4):
#         for r in range(3, -1, -1):
#             bowl.append(stackbowl[r][c])
#     fishes = bowl[:]
#     return fishes


# def solve(fishes, N):
#     fishes = fillFish(fishes, N)
#     fishes = stackBowl1(fishes, N)
#     fishes = stackBowl2(fishes, N)
#     return fishes

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# N, K = map(int, input().split())
# fishes = list(map(int, input().split()))
# ans = 0
# while max(fishes) - min(fishes) > K:
#     ans += 1
#     fishes = solve(fishes, N)
# print(ans)
    

