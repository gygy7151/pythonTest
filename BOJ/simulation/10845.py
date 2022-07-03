'''
큐
'''
import sys
input = sys.stdin.readline
def solution():
    ANS = []
    Q = []

    for _ in range(int(input().rstrip())):
        CMMD = input().rstrip()
        N = len(Q)
        if 'push' in CMMD:
            STR, X = CMMD.split()
            Q.append(int(X))
        
        elif CMMD == 'pop':
            ANS.append(Q.pop(0)) if N else ANS.append(-1)

        elif CMMD == 'size':
            ANS.append(len(Q))

        
        elif CMMD == 'empty':
            ANS.append(0) if N else ANS.append(1)

        
        elif CMMD == 'front':
            ANS.append(Q[0]) if N else ANS.append(-1)

        # backs
        else:
            ANS.append(Q[-1]) if N else ANS.append(-1)

    return ANS
res = solution()
print(*res, sep='\n')