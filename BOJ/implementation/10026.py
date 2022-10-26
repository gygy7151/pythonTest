'''
적록색약
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    graph = [list(input()) for _ in range(N)]

    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    nonBlindCnt, blindCnt = 0, 0
    nonBlindVisit, blindVisit = set(), set()
    nonBlindVisit.add((0,0))
    blindVisit.add((0,0))
    
    # 뎁스는 기본 1로 시작한다
    def nonBlind(x,y, color, depth):
        nonlocal nonBlindCnt
        nonlocal nonBlindVisit
        
        for i in range(4):
            nx, ny = x + dir[i][0], y + dir[i][1]

            if 0 <= nx < N and 0 <= ny < N:
                if (ny, nx) not in nonBlindVisit:
                    if graph[ny][nx] != color:
                        nonBlindCnt = max(depth+1, nonBlindCnt)
                        nonBlindVisit.add((ny, nx))
                        nonBlind(nx, ny, graph[ny][nx], depth+1)

                    
                    else:
                        nonBlindVisit.add((ny, nx))
                        nonBlind(nx, ny, color, depth)

    # 발강색,초록색은 하나로 본다
    def blind(x,y, color, depth):
        nonlocal blindCnt
        nonlocal blindVisit

        for i in range(4):
            nx, ny = x + dir[i][0], y + dir[i][1]

            if 0 <= nx < N and 0 <= ny < N:
                newColor = graph[ny][nx]
                if (ny, nx) not in blindVisit:
                    if newColor != color:
                        if color == 'B':
                            blindCnt = max(depth+1, nonBlindCnt)
                            blindVisit.add((ny, nx))
                            blind(nx, ny, graph[ny][nx], depth+1)
                    
                    else:
                        blindVisit.add((ny, nx))
                        blind(nx, ny, color, depth)
            
    nonBlind(0,0,graph[0][0], 1)
    blind(0,0,graph[0][0], 1)
    print(nonBlindCnt, blindCnt)

solution()
        