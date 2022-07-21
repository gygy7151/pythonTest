'''
DSLR
'''
'''
두번째풀이 -아..조건을 잘못이해했구나
'''
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    q= deque()
    q.append((A, ""))
    visit = [False] * 10000
# n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)


    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == B:
            print(path)
            break

        num1 = (2*num)%10000
        if not visit[num1]:
            q.append((num1, path+"D"))
            visit[num1] = True

        num2 = (num-1)%10000
        if not visit[num2]:
            q.append((num2, path+"S"))
            visit[num2] = True

        num3 = (10*num+(num//1000))%10000
        if not visit[num3]:
            q.append((num3, path+"L"))
            visit[num3] = True

        num4 = (num//10+(num%10)*1000)%10000
        if not visit[num4]:
            q.append((num4, path+"R"))
            visit[num4] = True




'''
첫번째풀이 - 틀림
'''

# import sys
# input = sys.stdin.readline

# def solution():
    
#     for _ in range(int(input())):
#         ANS = []
#         A,B = input().rsplit()

#         #D
#         numD = int(A)
#         cntD = 0
#         while numD != int(B) and cntD < 10000:
#             numD *= 2
#             cntD += 1
#             if numD > 9999:
#                 numD = numD % 10000
#         if cntD != 0 and numD == int(B):
#             ANS.append('D'*cntD)

#         #S
#         numS = int(A)
#         cntS = 0
#         while numS != int(B) and numS >= 0:
#             numS -= 1
#             cntS += 1
#             if numS == 0:
#                 numS = 9999
#                 break
#         if cntS != 0 and numS == int(B):
#             ANS.append('S'*cntS)

#         #L
#         #불변객체네..
#         numL = A

#         cntL = 0
#         while int(numL) != int(B) and cntL <= 4:
#             if len(numL) == 4:
#                 numL = numL[1:] + numL[0]
            
#             elif len(numL) == 3:
#                 numL += '0'
                
#             elif len(numL) == 2:
#                 numL = '0' + numL + '0'
            
#             else:
#                 numL = '00' + numL + '0'
            
#             cntL += 1
            
#         if cntL != 0 and int(numL) == int(B):
#             ANS.append('L'*cntL)

#         #R
#         numR = A
#         cntR = 0
#         while int(numR) != int(B) and cntR <= 4:
#             if len(numR) == 4:
#                 numR = numR[-1] + numR[0:-1]

#             elif len(numR) == 3:
#                 numR = numR[-1] + '0' + numR[0:2]

#             elif len(numR) == 2:
#                 numR = numR[-1] + '00' + numR[0]

#             else:
#                 numR = numR[0] + '000'
#             cntR += 1

#         if cntR !=0 and int(numR) == int(B):
#             ANS.append('R'*cntR)

#         ANS.sort(key=lambda x: len(x))
#         # print(ANS)
#         if len(ANS):
#             print(ANS[0])

# solution()
