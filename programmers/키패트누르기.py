'''
키패드누르기
'''
'''
첫번째풀이
'''
def solution(numbers, hand):
    ANS = ''
    MEMO = {}
    DIAL = [
               ['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9'],
               ['*', '0', '#']
           ]
    
    L, R = (3,0), (3,2)

    for i in range(4):
        for j in range(3):
            MEMO[DIAL[i][j]] = (i,j)
    
    # pop(0)하면 O(N)시간걸려서 그냥 i인덱스로 접근함
    for i in range(len(numbers)):
        N = numbers[i]
        
        if N == 1 or N == 4 or N == 7:
            ANS += 'L'
            L = MEMO[str(N)]
        
        elif N == 3 or N == 6 or N == 9:
            ANS += 'R'
            R = MEMO[str(N)]
        
        else:
            LDIFF = (abs(MEMO[str(N)][0] - L[0]) + abs(MEMO[str(N)][1] - L[1]))
            RDIFF = (abs(MEMO[str(N)][0] - R[0]) + abs(MEMO[str(N)][1] - R[1]))
            
            if LDIFF == RDIFF:
                if hand == 'left':
                    ANS += 'L'
                    L = MEMO[str(N)]
                else:
                    ANS += 'R'
                    R = MEMO[str(N)]

            elif LDIFF < RDIFF:
                ANS += 'L'
                L = MEMO[str(N)]

            else:
                ANS += 'R'
                R = MEMO[str(N)]

    return ANS

 