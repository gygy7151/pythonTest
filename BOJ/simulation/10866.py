'''
덱
'''
import sys
input = sys.stdin.readline
def solution():
    DEQUE = []
    ANS = []

    for _ in range(int(input().rstrip())):
        CMMD = list(map(str, input().rstrip().split()))
        N = len(DEQUE)
        if len(CMMD) == 1:
            if CMMD[0] == 'pop_front':
                if N:
                    ANS.append(DEQUE.pop(0))
                    
                else:
                    ANS.append(-1)

            elif CMMD[0] == 'pop_back':
                if N:
                    ANS.append(DEQUE.pop())
                
                else:
                    ANS.append(-1)

            elif CMMD[0] == 'size':
                ANS.append(len(DEQUE))

            elif CMMD[0] == 'empty':
                if not N:
                    ANS.append(1)
                else:
                    ANS.append(0)

            elif CMMD[0] == 'front':
                if N:
                    ANS.append(DEQUE[0])
                else:
                    ANS.append(-1)

            #'back'
            else:
                if N:
                    ANS.append(DEQUE[-1])
                else:
                    ANS.append(-1)

        else:
            STR, X = CMMD
            if STR == 'push_front':
                DEQUE.insert(0, X)

            else:
                DEQUE.append(X)
    return ANS
res = solution()
print(*res, sep='\n')