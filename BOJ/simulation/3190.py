'''
뱀
기어다니다가 사과를 먹으면 길이 늘어나고
벽 또는 자기 자신의 몸과 부딪히면 게임 끝

보드크키는 N * N
K : 사과의개수
L : 뱀의 방향 변환 횟수  1 <= L <= 100
    게임 시작 시간으로부터 X초가 끝난 뒤 | 왼쪽(L) or 오른쪽(D)로 90도 회전
    X는 10000이하 양의 정수임

    사과위치는 머리부분만 확인하면 됨
    interupt 메모이제이션으로?
A : 사과위치
1 : 뱀위치
0 : 뱀없는위치
'''
N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())

# 사과표시
for _ in range(K):
    x, y = map(int, input().split())
    #사과인덱스를 보드에 맞춰줘야됨 ***실수
    board[x-1][y-1] = 'A'

# 방향 변환정보 저장 인터럽트 인덱스 i == i초가 끝난뒤
# **아...실수...interupt는 뱀의 방향횟수가 아닌 최대 X초를 길이로 삼아야했다..
interupt = [0]*10001 
L = int(input())
for _ in range(L):
    cnt, d = map(str, input().split())
    interupt[int(cnt)] = d

t = 0
# 초기 뱀위치 표시 0번째요소가 꼬리, 맨마지막요소가 머리
snake = [(0,0)]
dir = [(0,1),(1,0),(0,-1),(-1,0)] # 동 남 서 북
s_d = 0
dx, dy = 0, 1
# 뱀이동
while True:
    
    #이동시작
    if (t + 1) > 10000:
        break
    else:
        t += 1
    # 머리 추가
    nx, ny = (snake[-1][0] + dx), (snake[-1][1]+ dy)
    # 벽과 부딪히면 게임종료       
    if nx < 0 or N <= nx or ny < 0 or N <= ny:
        break
    if 0 <= nx < N and 0 <= ny < N:
        # 만약 자기자신과 부딧히면 종료
        if (nx,ny) in snake:
            break
        snake.append((nx,ny))
        
        # 사과가 존재하면
        if board[nx][ny] == 'A':
            # 꼬리그대로 사과만 없앰
            board[nx][ny] = 0
        else:
            # 꼬리위치한칸 비워줌
            snake.pop(0)
        
        # t초가 끝난후에 방향 변환정보 확인
        # 왼쪽 또는 오른쪽 방향에 맞게 인덱스 변환
        if interupt[t] == 'L':
            # 왼쪽 90도
            if s_d == 0:
                s_d = 3
            else:
                s_d -= 1
        elif interupt[t] == 'D':
            # 오른쪽 90도
            if s_d == 3:
                s_d = 0
            else:
                s_d += 1
        
        # 방향정보 갱신
        dx, dy = dir[s_d][0], dir[s_d][1]


# 몇초에 종료되었는지 출력
print(t)

    













