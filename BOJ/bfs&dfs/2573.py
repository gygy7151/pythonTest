'''
빙산 - 2573번
0이 접해있는 수만큼 차감됨
두덩어리 이상으로 분리되는 최초의 시간을 구하는 프로그램을 작성하라
3 <= N,M <= 300
0 <= h <= 10
요소는 인덱스1부터 n-1까지만 접근하면된다
[전략1]
그래프 사본을 만들고
거기서 0이 아닌요소들만 따로 pos리스트에 담고
그 요소들만 계속 접근하면서
세부조건에 맞으면 해당요소인덱스의 값을 -1해주고
전체한바퀴 돌면 +1년해주고
그다음에 2묶음되는지 bfs로 돌리고 
q가 끊기면 cnt+1 해서
cnt가 2가되면 while문을 종료했지.

녹는 조건이 뭐야
ice[nx][ny] temp[nx][ny] 모두 0보다 큰상태여야됨. 반드시 4번도는동안 temp[i][j]는 음수가 될 수 있기때문에.

[전략2] 메소드 사용하지 않고 복사하기
check = [] 새로운 변수선언해서 그래프만든다.
N번만큼 ice[i]값 append 해서 대입해줘서 값을 할당해. 이건 메모리주소 참조중복없음. -> 그래도 확인해봐.
bfs로 접근할껀데

while True: 
멜팅메소드
출발요소 값이 0보다 크면,
상하좌우로 ice그래프에서 움직이면서
범위벗어나지 않고
이동한인덱스 값이 0이고 check가 0보다 크면 check[i][j]는 -1해준다.
check[i][j]가 0이면 graph[i][j]도 0으로 치환해줘야됨.
그리고 time + 1
한다음 bfs로 돌려서 묶음 2개인지 확인하기

[전략3] 시간초과 해결하기
pos에서 방문한것 저장하고 방문하는 형식으로 했음

아.. 빙하가 있는지 없는지 체크하는 걸 안했다. 아닌데 했는데?
만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.
이조건을 안했음 ㅋㅋ
'''
N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
pos = []
for i in range(N):
    for j in range(M):
        if ice[i][j] != 0:
            pos.append((i,j))
dir = ((-1,0), (1,0), (0,-1), (0,1))
def count_ice():
    visited = [[False]* M for _ in range(N)]
    check = False
    q = []
    for p in pos:
        l, m = p[0], p[1]
        if ice[l][m] != 0 and not visited[l][m]:
                if check:
                    return True
                q.append((l,m))
                visited[l][m] = 1
                while q:
                    x, y = q.pop(0)
                    for d in dir:
                        nx = x + d[0]
                        ny = y + d[1]
                        if 0<= nx < N and 0<= ny < M:
                            if ice[nx][ny] != 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                check = True
    return False
def melt():
    # print('녹는다')
    q = [[0] * M for _ in range(N)]
    for p in pos:
        x, y = p[0], p[1]
        if ice[x][y] != 0:
            for d in dir:
                nx = x + d[0]
                ny = y + d[1]
                if 0 <= nx < N and 0 <= ny < M:
                    if ice[nx][ny] == 0:
                        q[p[0]][p[1]] += 1
    # print('뺄애들')
    for p in pos:
        r, k = p[0], p[1]
        if ice[r][k] == 0:
            continue
        ice[r][k] -= q[r][k]    
        if ice[r][k] < 0:
            ice[r][k] = 0
    # for i in range(N):
    #     print(ice[i])

def check_ice():
    cnt = 0
    for p in pos:
        r, k = p[0], p[1]
        if ice[r][k] != 0:
            return True
    return False

year = 0
while not count_ice():
    if not check_ice():
        year = 0
        break
    year += 1
    melt()
print(year)







# N, M =  map(int, input().split())
# ice = [list(map(int, input().split())) for _ in range(N)]
# check = []
# pos = []
# time = 0

# for i in range(N):
#     check.append(ice[i])
# dir = ((-1,0), (1,0), (0,-1), (0,1))

# for i in range(N):
#     for j in range(M):
#         if ice[i][j] != 0:
#             pos.append((i,j))

# def melt(time):
#     print('까꽁?')
#     for p in pos:
#         if ice[p[0]][p[1]] > 0:
#             for d in dir:
#                 ni = p[0] + d[0]
#                 nj = p[1] + d[1]
#                 if 0<= ni < N and 0<= nj < M:
#                     if ice[ni][nj] == 0 and check[p[0]][p[1]] > 0:
#                         check[ni][nj] -= 1

#     for i in range(N):
#         for j in range(M):
#             if check[i][j] == 0:
#                 ice[i][j] = 0
#     time += 1

# def bfs(x, y, ice_visited):
#     q = []
#     q.append((x,y))
#     ice_visited[x][y] = 1
#     while q:
#         r, k = q.pop(0)
#         for d in dir:
#             nr = r + d[0]
#             nk = k + d[1]
#             if 0<= nr < N and 0<= nk < M:
#                 if ice[nr][nk] > 0 and not ice_visited[nr][nk]:
#                     ice_visited[nr][nk] = 1
#                     q.append((nr, nk))

# while True:
#     melt(time)
#     cnt = 0
#     ice_visited = [[0]*M for _ in range(N)]
#     for p in pos:
#         if ice[p[0]][p[1]] > 0 and not ice_visited[p[0]][p[1]]:
#             bfs(p[0], p[1], ice_visited)
#             cnt += 1
#             print(cnt)
#         if cnt == 2:
#             print(time)
#             break
#         if cnt == 0:
#             print(0)


# import copy
# N, M =  map(int, input().split())
# ice = [ list(map(int, input().split())) for _ in range(N)]
# temp = copy.deepcopy(ice)
# pos = []
# for i in range(N):
#     for j in range(M):
#         if ice[i][j] != 0:
#             pos.append((i,j))
# dir = ((-1,0), (1,0), (0,-1), (0,1))
# def melt(temp):
#     global ice
#     for p in pos:
#         #ice 각요소는 반드시 상하좌우 모든영역을 확인해야된다. 이미 방문한곳도 다시 들려야됨 0이있으면 -1해야하기때문.
#         if ice[p[0]][p[1]] > 0 and temp[p[0]][p[1]] > 0:
#             for d in dir:
#                 nx = p[0] + d[0]
#                 ny = p[1] + d[1]
#                 if ice[nx][ny] == 0:
#                     temp[p[0]][p[1]] -= 1
#     ice = copy.deepcopy(temp)

# def bfs(x, y):
#     global ice_visited
#     q = []
#     q.append((x,y))
#     ice_visited[x][y] = 1
#     num = 0
#     while q:
#         r, k = q.pop(0)
#         for d in dir:
#             nr = r + d[0]
#             nk = k + d[1]
#             if ice[nr][nk] > 0 and not ice_visited[nr][nk]:
#                 ice_visited[nr][nk] = 1
#                 q.append((nr, nk))
#                 num += 1
#         if num == 0:
#             return False
        
#         else:
#             return True

# def check():
#     global pos
#     pos = []
#     for i in range(N):
#         for j in range(M):
#             if ice[i][j] != 0:
#                 pos.append((i,j))
            
# time = 0
# while len(pos) > 0 :
#     print(len(pos))
#     check()
#     melt(temp)
#     cnt = 0
#     time += 1
#     ice_visited = [[0]*M for _ in range(N)]
#     for p in pos:
#         if ice[p[0]][p[1]] > 0:
#             # print(ice_visited)
#             bfs(p[0], p[1])
#             cnt += 1
#             if cnt == 2:
#                 print(time)
#                 break

#             if cnt == 0:
#                 print(0)
#                 break

##깊은복사 얕은복사.
#temp에 ice를 할당하면 값이 할당되는것이 같은 메모리주소를 바라보게 된다.
#그래서 temp를 변경하면 ice도 같이 바뀌는거야 왜? 메모리주소가 같으니까 ㅋㅋㅋ
#일반적으로 리스트는 mutable한 객체인데 mutable한 객체는 순서가 있다.
# 뭐 슬라이싱으로 temp = ice[:] 이렇게 값을 할당해주면 둘다 1차원 리스트 인경우 서로 다른 메모리주소를 참조하여 값이 a값이 b에 영향을 주지 않는다.
# 하지만 리스트안에 또 다른 리스트 또는 mutable한 객체가 들어가면 문제가 된다. 왜? 그 내부객체는 같은 주소를 바라보고 있게 되거든
# id[ice] !=  id[temp] 인데반해, id[ice[0]] = id[temp[0]] 임. 근데 그냥 재할당인경우엔 상관없음
# 근데 값에 뭘 더해주거나 빼주거나 이런건 값을 변경하는 것이므로 temp의 값을 바꾸면 ice도 따라 바뀌게됨
# 그래서 위와같은 얕튼복사 대신에 깊은복사는 어케 해결하냐?
# copy.deepcopy메소드를 통해 해결하면 됨
# 근데 메소드 안쓰고 하려면 아까처럼 그 그래프에서 0이되는 곳을 따로 메모이제이션 해주는 방법이 있음
# 이방법으로 다시 풀어봐야될듯. 메소드 사용안되는곳이 대부분이니까.
    
