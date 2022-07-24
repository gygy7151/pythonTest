'''
DSLR
'''
'''
세번째풀이 - BFS를 유지하되 방문여부 처리를 해시테이블 set을 활용-python3(x),pypy(0)
'''
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())
    q = deque([(A, "")])
    visited = set()

    def left(n):
        front = n % 1000
        back = n // 1000
        res = front*10 + back
        return res

    def right(n):
        front = n % 10
        back = n // 10
        res = front*1000 + back
        return res

    def double(n):
        res = n*2
        if res > 9999:
            res %= 10000
        return res

    def slice(n):
        res = n
        if res == 0: return 9999
        res -= 1
        return res

    while q:
        num, path = q.popleft()
        visited.add(num)
        
        if num == B:
            print(path)
            break

        # D
        num1 = double(num)
        if num1 not in visited:
            q.append((num1, path+"D"))
            visited.add(num1)

        # S
        num2 = slice(num)
        if num2 not in visited:
            q.append((num2, path+"S"))
            visited.add(num2)

        # L
        num3 = left(num)
        if num3 not in visited:
            q.append((num3, path+'L'))
            visited.add(num3)

        # R
        num4 = right(num)
        if num4 not in visited:
            q.append((num4, path+'R'))
            visited.add(num4)

'''
두번째풀이 -아..조건을 잘못이해했구나 - 그런데도 시간초과
'''
# from collections import deque
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     A, B = map(int, input().split())
#     q= deque()
#     q.append((A, ""))
#     visit = [False] * 10000
# # n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)


#     while q:
#         num, path = q.popleft()
#         visit[num] = True
#         if num == B:
#             print(path)
#             break

#         num1 = (2*num)%10000
#         if not visit[num1]:
#             q.append((num1, path+"D"))
#             visit[num1] = True

#         num2 = (num-1)%10000
#         if not visit[num2]:
#             q.append((num2, path+"S"))
#             visit[num2] = True

#         num3 = (10*num+(num//1000))%10000
#         if not visit[num3]:
#             q.append((num3, path+"L"))
#             visit[num3] = True

#         num4 = (num//10+(num%10)*1000)%10000
#         if not visit[num4]:
#             q.append((num4, path+"R"))
#             visit[num4] = True




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
