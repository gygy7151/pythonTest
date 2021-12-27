'''
상하좌우
여행가 A는 N*N크기의 정사각형
공간위에 있다.
가장 오른쪽 아래 좌표는 (N,N)에 해당
여행가는 A는 상,하,좌,우 방향으로 이동가능
시작 좌표는 항상 (1,1)
여행가 A가 최종적으로 도착할 지저믜 좌표를 구하라
'''

n = int(input())

def solution(n):

    #현재 위치 만들어주고
    x, y = 1, 1
    #n^n 배열을 만들어주고
    map = [[0]* n for _ in range(n)]
    #사용자 발걸음 위치를 받는 리스트를 만들고
    steps = input().split() # split()은 리스트로 데이터를 띄워쓰기로 구분해서 받는다.
    print(steps)
    point = {'L': (0, -1), 'R': (0,1), 'U': (-1,0), 'D': (1,0)}

    #리스트요소에 하나씩 접근해서
    for step in steps :
        print(step)
    #L(0,-1), R(1,0), U(0,-1), D(0, 1) 이면 만큼 기존 위치에 더해줌
        if x >= 1 or y >= 1 or x <= n or y <= n :

            if step == 'L' or step =='U':
                pass

            else :   
                x += point[step][0]
                print(x, 'x 값이 변경되었습니다.')
                y += point[step][1]
                print(y, 'y 값이 변경되었습니다.')
        
        else :
            x += point[step][0]
            print(x, 'x 값이 변경되었습니다.')
            y += point[step][1]
            print(y, 'y 값이 변경되었습니다.')
            



    print(x, y)
    #result

solution(n)