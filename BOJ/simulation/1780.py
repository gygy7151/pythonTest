'''
종이의개수
'''
'''
첫번째풀이 - 하나라도 target과 값이 다르면 cut해주고 return 해줄것. 이거 기억하자.
'''
import sys
input = sys.stdin.readline

def solution():    
    N = int(input())
    MEMO = {-1:0, 0:0, 1:0}

    if N == 1:
        MEMO[int(input())] += 1
        return list(MEMO.values())
    
    PAPER = []
    for _ in range(N):
        PAPER.append(list(map(int, input().split())))

    def cut(x,y,l):
        nonlocal MEMO
        target = PAPER[x][y]

        for i in range(x, x+l):
            for j in range(y, y+l):
                if PAPER[i][j] != target:

                    cut(x, y, l//3) #1사분면
                    cut(x, y+(l//3)*1, l//3) #2사분면
                    cut(x, y+(l//3)*2, l//3) #3사분면
                    cut(x+(l//3)*1, y, l//3) #4사분면
                    cut(x+(l//3)*1, y+(l//3)*1, l//3) #5사분면
                    cut(x+(l//3)*1, y+(l//3)*2, l//3) #6사분면
                    cut(x+(l//3)*2, y, l//3) #7사분면
                    cut(x+(l//3)*2, y+(l//3)*1, l//3) #8사분면
                    cut(x+(l//3)*2, y+(l//3)*2, l//3) #9사분면
                    #와..아찔했다. 이거 잊지말자
                    return
    
        # 모두일치하는경우
        MEMO[target] += 1

    cut(0,0,N)
    return list(MEMO.values())
res = solution()
print(*res, sep="\n")