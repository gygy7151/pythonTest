'''
왕실의 나이트
왕실정원은 8 x 8
열행 a1

1.수평으로 두칸이동 (1, 2) (-1, 2) (1, -2) (-1, -2)
2.수직으로 두칸이동 (2, 1) (-2, 1) (2, -1) (2, 1)

행위치는 1부터 8까지이며
열위치는 a부터 h까지임 a b c d e f g h

특정위치에서 이동할 수 있는 경우의 수를 모두 구하는 문제

'''

point = input()

def solution(point):

    # 뭘해야할까?
    # 현재 위치저장해야되고 x, y는 input으로 입력받음 map(int, input().split()) v
    # 8x8 빈배열부터 만들고 v
    # 입력받은 경로까지 이중 for문 돌리고
    # 범위에서 벗어나는지 여부 체크 조건문
    ## 벗어나지 않으면 어캄? count += 1
    ## 만약 벗어나면? count하지 않고 그냥 pass
    ## ord() 문자열 -> 아스키코드 chr() 아스키코드 -> 문자열

    #소문자 a-z의 문자열 출력
    #for x in range(97,123):
	#print(chr(x),end="")
    count = 0

    #행
    x = int(point[1])
    #열
    y = point[0]

    board = [ (i+1, chr(j)) for i in range(8) for j in range(97, 105) ]

    #수평으로 두칸이동한 뒤 수직으로 한칸이동
    #수직으로 두칸 이동한 뒤 수평으로 한칸 이동
    steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, 2)]

    for step in steps :
        nx = int(point[1])
        ny = point[0]

        nx += int(step[0])
        ny = chr(ord(ny) + step[1])
        print(nx,ny, '(x,y)값')

        for data in board :
            if (nx, ny) == data:
                count += 1
                print(count, 'count가 추가되었습니다.')
                nx = int(point[1])
                ny = point[0]

    print(count)
    
solution(point)