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
    gameboard = [ [0] * m  for _ in range(n)]

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

    # 방향 리스트
    dir = {'0' : [-1, 0], '1' : [0, 1], '2' : [1, 0], '3': [0, -1]}
    
    # 방향이동 카운트
    dcount = 0

    # 방문한 리스트
    visitList = []
    visitList.append((x, y))

    # 캐릭터이동은 mcount가 5보다 작을때까지만
    # 0 -> 3 // 3 -> 2 // 2 -> 1 // 1 -> 0
    # 0 + 3 // (3 + 3) % 4 = 2 // (2 + 3) % 4 = 1 // (1 + 3) % 4 = 0
    # (n + 3) % 4 = 다음방향
    while dcount < 5 :

        #비교위치를 캐릭터 현재위치로 초기화 해준다
        cx, cy = dx, dy
        
        #현재방향 업데이트(반시계방향)
        ds = (ds + 3) % 4
        print(ds, '현재방향')
        
        #비교위치 업데이트-> 반복되는걸 줄여준다.
        # 여기도 cx = dx + dir[str(ds)][0]
        # # 여기도 cy = dy + dir[str(ds)][1] 로 해주면 72번코드가 필요없다.
        cx += dir[str(ds)][0]
        cy += dir[str(ds)][1]
        print('비교위치 업데이트완료',cx, cy)

        # count 추가
        dcount += 1

        #해당 비교칸 방문여부체크
        try :
            visitList.index((cx, cy))
        
        except ValueError :

        # 바다면 이동하지 않는다. 또는 행렬값이 out of range이면 이동하지 않는다
        # 만약 방문한적 없으면 이동한다( = 육지 )
            if gameboard[cx][cy] == 0 :
            # dcount는 초기화한다
                dcount = 0

            # 현재 좌표 방문 처리
                visitList.append((cx, cy))
                print('방문완료위치 추가완료')

        # 현재 위치를 업데이트한다.(비교위치를 현재위치에 대입)
                dx, dy = cx, cy
                print('현재 캐릭터 위치는 (%d, %d)입니다.' %(dx, dy))

                print('현재 캐릭터가 방문한 칸의 수는 {}칸입니다.'.format(len(visitList)))


        # dcount가 초과되었을때 한번더 체크할 내용
        # 바다로 막혀있으면 그냥 그대로 pass
        # 바다로 안막혀있는 경우 이동하기        
        if dcount == 4 :
            
            dds = 0

            #뒤쪽방향 임시변수선언
            if ds < 2 :
                
                dds = ds + 2

            elif ds >= 2:
                dds = ds - 2
            
            print('dds는 {}입니다.'.format(dds))

            #비교위치 임시 업데이트
            dx += dir[str(dds)][0]
            dy += dir[str(dds)][1]
            print('뒤로한칸 이동한 현재위치',dx, dy) 

            #뒤쪽 위치가 육지가 아닐때
            if gameboard[dx][dy] == 1 :
                print('뒤로이동한칸이 바다이므로 종료합니다.')
                break
            
            # 방문한 위치 추가할 필요없음. 이미 방문한 칸으로 back하는거임

            # dcount 초기화
        
            else :
                dcount = 0

    
    return len(visitList)

if __name__ == '__main__' : 

    count = solution(n,m,x,y,d)
    print('캐릭터가 방문한 최종 칸의 수는 %d입니다' %count)