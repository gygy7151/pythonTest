'''
빙고 체크하기
일간.주간.월간 업데이트 - 이걸 놓쳤네...
그리고 처음 입력값이 (일자,성공한미션) 이렇게 입력되는 줄 모르고 접근함..
문제를 대충 읽었다는 소리임
어떻게 풀지 논리 구현한다음 다시 문제 읽어보면서 해당 입력조건값에 맞춰서 논리를 짰는지
반드시!!!! 반드시!!!!!!!!!!!체크하고 구현으로 넘어가야됨 ㅠ
문제 처음 부터 끝까지 정독 필수임......
'''
'''
일반 빙고는 1~9번 미션
주간 빙고는 10~18번 미션
월간 빙고는 19~27번 미션으로 구성됨
미션을 성공할때마다 해당칸에 체크표시
가로, 세로, 대각선으로 연속된 3개의 체크를 만들때 1점을 얻음
3개 체크 연속되서 1점 얻으면 해당 부분 지워줘야됨
모든 빙고는 3*3 형태임
가로: x-1, x, x+1 (y는 0~2, x는 항상 1) 
세로: y-1, y, y+1 (x는 항상1 y는 0~2) 
대각선: [(y-1,x-1), (x,y), (x+1, y+1)], [(y+1,x-1),(x,y), (x+1,y-1)] (x,y는 항상1)

12월 한달동안 유저가 미션을 성공한 기록을 담은 2차원 정수 배열 logs가 입력조건임
유저가 총 몇점을 얻었는지 리턴하는 함수를 완성하셈

미션 완료 체크판 bingo
총 점수 answer
logs를 0번째 인덱스부터 돌면서 해당 미션 완료한 내용 bingo판에 표시
check 함수에 가로,세로,대각선 빙고되는지 체크하고 만약 빙고라면 해당 체크 표시 지우고 cnt + 1
빙고함수 결과만큼 answer에 더해줌

아... 요일별로

'''
def solution(logs):
    answer = 0
    bingoD = [[0 for _ in range(3)] for _ in range(3)]
    bingoW = [[0 for _ in range(3)] for _ in range(3)]
    bingoM = [[0 for _ in range(3)] for _ in range(3)]

    day = set([ x for x in range(1, 10)])
    week = set([ x for x in range(10, 19)])
    month = set([ x for x in range(19, 28)])

    # 0번째 가로빙고, 1번째 세로빙고, 2번째 대각선빙고
    checkD = [[0 for _ in range(3)] for _ in range(3)] 
    checkW = [[0 for _ in range(3)] for _ in range(3)]
    checkM = [[0 for _ in range(3)] for _ in range(3)]


    link = {
        1: (0,0),
        2: (0,1),
        3: (0,2),
        4: (1,0),
        5: (1,1),
        6: (1,2),
        7: (2,0),
        8: (2,1),
        9: (2,2)
    }

    def check(param):
        nonlocal bingoD
        nonlocal bingoW
        nonlocal bingoM
        cnt = 0

        if param == 'D':
            for y in range(3):
                if bingoD[y][0] == 1 and bingoD[y][1] == 1 and bingoD[y][2] == 1:
                    if not checkD[0][y]:
                        cnt += 1

            for x in range(3):
                if bingoD[0][x] == 1 and bingoD[1][x] == 1 and bingoD[2][x] == 1:
                    if not checkD[1][y]:
                        cnt += 1

            if bingoD[0][0] == 1 and bingoD[1][1] == 1 and bingoD[2][2] == 1:
                if not checkD[2][0]:
                    cnt += 1

            if bingoD[2][0] == 1 and bingoD[1][1] == 1 and bingoD[0][2] == 1:
                if not checkD[2][1]:
                    cnt += 1


        elif param == 'W':
            for y in range(3):
                if bingoW[y][0] == 1 and bingoW[y][1] == 1 and bingoW[y][2] == 1:
                    if not checkW[0][y]:
                        cnt += 1

            for x in range(3):
                if bingoW[0][x] == 1 and bingoW[1][x] == 1 and bingoW[2][x] == 1:
                    if not checkW[1][y]:
                        cnt += 1

            if bingoW[0][0] == 1 and bingoW[1][1] == 1 and bingoW[2][2] == 1:
                if not checkW[2][0]:
                    cnt += 1

            if bingoW[2][0] == 1 and bingoW[1][1] == 1 and bingoW[0][2] == 1:
                if not checkW[2][1]:
                    cnt += 1

        else:
            for y in range(3):
                if bingoM[y][0] == 1 and bingoM[y][1] == 1 and bingoM[y][2] == 1:
                    if not checkM[0][y]:
                        cnt += 1


            for x in range(3):
                if bingoM[0][x] == 1 and bingoM[1][x] == 1 and bingoM[2][x] == 1:
                    if not checkM[1][y]:
                        cnt += 1

            if bingoM[0][0] == 1 and bingoM[1][1] == 1 and bingoM[2][2] == 1:
                if not checkM[2][0]:
                    cnt += 1

            if bingoM[2][0] == 1 and bingoM[1][1] == 1 and bingoM[0][2] == 1:
                if not checkM[2][1]:
                    cnt += 1

        return cnt


    date = [[] for _ in range(32)]

    for today, mission in logs:
        date[today].append(mission)


    for log in date:
        if log:
            # 일, 주, 월 미션 성공 여부 체크한다

            for successM in log:
                if successM in day:
                    x, y = link[successM]
                    bingoD[x][y] = 1

                elif successM in week:
                    x, y = link[successM - 9]
                    bingoW[x][y] = 1

                elif successM in month:
                    x, y = link[successM - 18]
                    bingoM[x][y] = 1
    # 빙고 체크
    answer += check('D')
    answer += check('W')
    answer += check('M')



    return answer
