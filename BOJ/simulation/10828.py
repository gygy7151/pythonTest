'''
스택
'''
'''
두번째풀이 - 함수형 프로그래밍
그냥 단순히 c.strip()하면 안됨.. 해당 문자열이 메소드 적용된 객체 참조해줘야됨
'''

import sys
def solution():
    ANS = []
    S = []
    CMMD = dict(
        push=lambda x: S.append(x),
        pop=lambda: S.pop() if S else -1,
        size=lambda: len(S),
        # 아..empty일땐 -1이 아니라 1을 반환해야한다.
        empty=lambda: 0 if S else 1,
        top=lambda: S[-1] if S else -1
    )
    input = sys.stdin.readlines()
    # print(input)
    for c in input[1:]:
        #반드시 다시 대입해주어야한다.
        c = c.strip()
        if c[:4] == 'push':
            CMMD['push'](c.split()[1])
        else:
            ANS.append(CMMD[c]())
    return ANS
res = solution()
print(*res, sep='\n')



'''
첫번째풀이
'''
# import sys
# from sys import stdin
# input = sys.stdin.readline
# next()
# for line in stdin:
#     print(line.split())
# def solution():
#     ANS = []
#     S = []

#     for _ in range(int(input().rstrip())):
#         CMMD = input().rstrip()
#         N = len(S)
#         if 'push' in CMMD:
#             S.append(int(CMMD.split()[1]))
        
#         elif CMMD == 'pop':
#             ANS.append(S.pop()) if N else ANS.append(-1)

#         elif CMMD == 'size':
#             ANS.append(len(S))

        
#         elif CMMD == 'empty':
#             ANS.append(0) if N else ANS.append(1)

        
#         elif CMMD == 'top':
#             ANS.append(S[-1]) if N else ANS.append(-1)

#     return ANS
# res = solution()
# print(*res, sep='\n')