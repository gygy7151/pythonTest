'''
게임 개발
캐릭터 장소는 N x M 크기 직사각형
각 칸은 육지 또는 바다
각 칸은 (A, B)
A는 북쪽으로 떨어진 칸의 개수
B는 서쪽으로 떨어진 칸의 개수

구하고자 하는 것은 캐릭터가 방문한 칸의 수

현재 위치에서 왼쪽방향으로 갈곳을 정함

[기본전제조건]
캐릭터 위치는 처음엔 항상 육지이다.
입력예시에서 캐릭터는 북쪽을 바라보고 서있다.

[캐릭터 이동단계]
1단계.현재 위치에서 현재방향기준으로 왼쪽방향부터 차례대로 갈곳을 정한다
2단계.캐릭터의 바로왼쪽에 가보지 않은 칸이 존재하면 왼쪽으로 회전한다음 왼쪽으로 한칸 전진한다.
3단계.만약 왼쪽방향에 가보지 않은 칸이 없다면 왼쪽방향으로 회전만수행하고 1단계로 돌아간다.
4단계.만약 네 방향 모두 이미 가본칸이거나 바다로 되어있는 경우 바라보는 방향을 유지한채로 한칸뒤로 간다.
    그리고 다시 1단계로 돌아간다. (단, 뒤쪽 방향이 바다인 경우 움직임을 멈춘다.->게임종료)

[입력조건]

1. 첫째줄 : N M 크기 공백구분
2. 캐릭터좌표 A B 방향 d
- 0 : 북쪽
- 1 : 동쪽
- 2 : 남쪽
- 3 : 서쪽
3. 맵이 육지인지 바다인지 
- 0 : 육지
- 1 : 바다

'''

n, m = map(int, input().split())
a, b, d = map(int, input().split())

def solution(n, m, a, b, d):

    # n X m 빈배열부터 만들고 v
    board = [[0] * m ] * n
    count = 0
    toggle = 0

    print(a, '초기 a값')
    print(b, '초기 b값')
    print(d, '초기 d값')
    # board 좌표 (int)
    x, y = a, b

    #초기방향값
    # 북 동 남 서 : 0, 1, 2, 3
    steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    print('역순정렬완료')


    # 빈배열에 맵의 정보 할당
    for i in range(n) :
        board[i] = list(map(int, input().split()))

    print(board)

    # 반시계방향으로 캐릭터 이동범위 설정
    # 서남동북으로 이동방향셋팅
    # 북 동 남 서 : 0, 1, 2, 3

    # 서 남 동 북 : 3, 2, 1, 0

    while toggle < 1:
        
        steps.reverse()
        reverse_steps = steps 

        for i in range(len(reverse_steps)) :
            limit = 4

            #기본 시작점부터 카운트하므로 디폴트값은 1이된다
            count = 1

            x += reverse_steps[int(i)][0]
            y += reverse_steps[int(i)][1]
            d = (3 - i)

            if x >= 0 and y >= 0 and x < n and y < m :
                ## 육지이거나 한번도 방문하지 않은곳, 캐릭터 위치 이동 및 방향이동유지
                if board[x][y] == 0 or board[x][y] != 'x' :
            
                    #이동횟수 카운팅
                    limit -= 1
                    count += 1

                    #방문한곳 x로 값초기화
                    board[x][y] = 'x'

                    print('캐릭터 위치 이동완료했습니다.')
                    print('현재 캐릭터위치 : (%d, %d) | 방향 : %d' %(x, y, d))
        
                ## 바다인 경우 또는 이미 방문한 경우, 방향만 이동유지
                elif board[x][y] == 1 or board[x][y] == 'x' :

                    y -= reverse_steps[int(i)][1]
                    x -= reverse_steps[int(i)][0]
                    print('방향만 이동완료했습니다.')
                    print('현재 캐릭터위치 : (%d, %d) | 방향 : %d' %(x, y, d))
                    limit -= 1

                ## 이동을 아예 못한 경우, 방향만 유지 한채로 뒤로 한칸
                elif limit == 0 and count == 0 :
                    y -= reverse_steps[int(i)][1]
                    x -= reverse_steps[int(i)][0]
                    
                    if d == 0 or d == 1 :

                        #방향유지를 위해 신규변수선언
                        dir = str(d + 2)
                        x += reverse_steps[dir][0]
                        y += reverse_steps[dir][1]

                        if board[x][y] == 1 :
                            toggle = 1
                            break
                
                    elif d == 2 or d == 3 :
                        dir = (d - 2)
                        x += reverse_steps[dir][0]
                        y += reverse_steps[dir][1]
                        
                        if board[x][y] == 1 :
                            toggle = 1
                            break

            else :
                #다시 제자리로 원위치 // 맵의 외곽은 항상 바다로 되어있음
                y -= reverse_steps[int(i)][1]
                x -= reverse_steps[int(i)][0]


        if toggle == 1 :
            break

solution(n,m,a,b,d)