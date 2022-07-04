'''
스택
'''
import sys
input = sys.stdin.readline
def solution():
    ANS = []
    S = []

    for _ in range(int(input().rstrip())):
        CMMD = input().rstrip()
        N = len(S)
        if 'push' in CMMD:
            S.append(int(CMMD.split()[1]))
        
        elif CMMD == 'pop':
            ANS.append(S.pop()) if N else ANS.append(-1)

        elif CMMD == 'size':
            ANS.append(len(S))

        
        elif CMMD == 'empty':
            ANS.append(0) if N else ANS.append(1)

        
        elif CMMD == 'top':
            ANS.append(S[-1]) if N else ANS.append(-1)

    return ANS
res = solution()
print(*res, sep='\n')