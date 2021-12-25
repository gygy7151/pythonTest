'''
게임 개발
캐릭터 장소는 N x M 크기 직사각형
각 칸은 육지 또는 바다
각 칸은 (A, B)

[기본전제조건]
캐릭터 위치는 처음엔 항상 육지이다.
입력예시에서 캐릭터는 북쪽을 바라보고 서있다.


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

[캐릭터 이동단계]
1단계.현재 위치에서 현재방향기준으로 왼쪽방향부터 차례대로 갈곳을 정한다
2단계.캐릭터의 바로왼쪽에 가보지 않은 칸이 존재하면 왼쪽으로 회전한다음 왼쪽으로 한칸 전진한다.
3단계.만약 왼쪽방향에 가보지 않은 칸이 없다면 왼쪽방향으로 회전만수행하고 1단계로 돌아간다.
4단계.만약 네 방향 모두 이미 가본칸이거나 바다로 되어있는 경우 바라보는 방향을 유지한채로 한칸뒤로 간다.
    그리고 다시 1단계로 돌아간다. (단, 뒤쪽 방향이 바다인 경우 움직임을 멈춘다.->게임종료)
'''

n, m = map(int, input().split())
x, y, d = map(int, input().split())

def solution(n, m, x, y, d):

    # 우선 빈배열을 만들고
    gameboard = [ [ 0 for _ in range(m)]  for _ in range(n)]

    # 배열에 값을 다 채워 넣어줘야 된다
    for i in range(n):
        gameboard[i] = list(map(int, input().split()))

    # 현재 위치에서 서쪽 위치좌표랑 비교
    # 현재위치좌표 디폴트값
    dx, dy = x, y


    # 비교위치좌표 디폴트값
    cx, cy = x, y
    
    # 현재위치 
    ds = d

    # 방문한 위치 저장리스트
    visitedList = []

    # 방향 리스트
    dir = {'0' : [-1, 0], '1' : [0, 1], '2' : [1, 0], '3': [0, -1]}
    
    # 방향이동 카운트
    dcount = 0

    # 캐릭터이동 카운트
    mcount = 0

    # 캐릭터이동은 count가 4보다 작을때까지만

    while dcount < 4 :

        try :

            # 만약 현재 위치가 북쪽이면? 서쪽으로 방향이동
            if ds == 0 :
        
            #방향 업데이트
                ds = 3
        
            #비교위치 업데이트
                #cx, cy += dir['3'][0], dir['3'][1]

            # count 추가
                dcount += 1

            # 만약 현재 위치가 서쪽이면? 남쪽으로 방햐이동

            elif ds == 3 :

            #방향 업데이트
                ds = 2
        
            #비교위치 업데이트
                #cx, cy += dir['2'][0], dir['2'][1]

            # count 추가
                dcount += 1


            # 만약 현재 위치가 남쪽이면? 동쪽으로 이동
            elif ds == 2 :

            #방향 업데이트
                ds = 1
        
            #비교위치 업데이트
                #cx, cy += dir['1'][0], dir['1'][1]
            
            # count 추가
                dcount += 1
 

            # 만약 현재 위치가 동쪽이면?

            elif ds == 1 :

            #방향 업데이트
                ds = 0
        
            #비교위치 업데이트
                #cx, cy += dir['0'][0], dir['0'][1]

            # count 추가
                dcount += 1

            else :
                pass
            
        # 방문한적 있으면 이동하지 않는다.
            if visitedList.index((cx, cy)) :
            
                print('이미 방문한 칸입니다.')

            
        # 바다면 이동하지 않는다.
            elif gameboard[cx][cy] == (1, 1) :
                print('바다입니다')

        except ValueError :
        # 방문한적 없으면 이동한다

        # 방문한 좌표를 visitedList에 추가한다.
            visitedList.append((cx,cy))

        # 현재 위치를 업데이트한다.(비교위치를 현재위치에 대입)
            dx, dy = cx, cy
        
        # 캐릭터 이동 카운트 추가
            mcount += 1

            print('이동완료')

    return mcount

if __name__ == '__main__' : 

    count = solution(n,m,x,y,d)
    print('캐릭터가 방문한 최종 칸의 수는 %d입니다' %count)