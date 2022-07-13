'''
쿼드트리
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    SCREEN = [list(map(int, input())) for _ in range(N)]
    ZIP_FILE = []
    print(SCREEN)
    def zip(x,y,l):
        color = SCREEN[x][y]
        #추가 예외처리
        if l == 1:
            return color

        for i in range(x, x+l):

            for j in range(y, y+l):
                if color != SCREEN[i][j]:
                    ZIP_FILE.append('(')
                    #1사분면부터 순서대로 호출해야한다.안그럼 오답출력됨
                    zip(x, y, l//2) # 1사분면
                    zip(x+l//2, y, l//2) # 3사분면
                    zip(x, y+l//2, l//2) # 2사분면
                    zip(x+l//2, y+l//2, l//2) # 4사분면
                    ZIP_FILE.append(')')
                    #실수**하나라도 값이 다르면 함수종료하는거 잊지말기                    
                    return
        
        if color == 0:
            # 입력값들을 join해야하므로 str타입으로 0과 1을 넣어주기
            ZIP_FILE.append('0')
        else:
            ZIP_FILE.append('1')
    
    zip(0,0,N)
    return ''.join(ZIP_FILE)

print(solution())



