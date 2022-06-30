'''
요세푸스 문제 0 - join할때 입력받는 객체내부 요소는 int가 아닌 str이여야한다.
'''
def solution():

    N, K = map(int, input().split())
    MEMO = [0] * N
    ANS, L_ANS = [], 0
    IDX, CNT = -1, 0

    while L_ANS < N:
        if IDX == N-1:
            IDX = 0
        else:
            IDX += 1

        if MEMO[IDX] == 0:
            CNT += 1
            
            # *실수.. 방문체크를 놓쳤다. 조심하자
            if CNT == K:
                MEMO[IDX] = 1
                ANS.append(str(IDX+1))
                L_ANS += 1
                CNT = 0
    
    return ANS

res = solution()
R = ', '.join(res)
print('<'+R+'>')