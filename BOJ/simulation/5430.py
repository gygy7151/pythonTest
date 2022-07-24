'''
AC
'''
'''
두번째풀이
'''
from collections import deque
import re
def solution():
    for _ in range(int(input())):
        order = input()
        numCount = int(input())
        S = input().rstrip()[1:-1]
        print(S)
        arr = deque( x for x in S.split(','))
        # arr = deque(x for x in re.split('[^0-9]', input()) if x)


        if order.count('D') > numCount:
            print('error')
            continue
        
        p = 0

        for action in order:
            if action == 'R':
                p += 1

            else:
                if p % 2:
                    arr.pop()
                else:
                    arr.popleft()

        if p % 2 == 1:
            arr.reverse()

        print(list(arr))

solution()


'''
첫번째/네번째풀이 - 33%에서틀림/ 해결..출력형식이 리스트가 아니라 스트링이었음 ㅠㅠ하..
'''
# from collections import deque
# import re
# def solution():
#     T = int(input())
#     if T == 0:
#         print('eroor')
#         return
#     for _ in range(T):
#         dirLeft = True
#         F = input()
#         N = int(input())
#         X = input()
#         X = deque( x for x in re.split('[^0-9]', X) if x)

#         for f in F:

#             if f == 'R':

#                 if dirLeft:
#                     dirLeft = False
#                 else:
#                     dirLeft = True

#             else:
#                 if not X:
#                     print('error')
#                     break

#                 if dirLeft:
#                     X.popleft()
                
#                 else:
#                     X.pop()
#         else:
#             if dirLeft:
#                 print('[' + ','.join(list(X)) + ']')
#             else:
#                 print('[' + ','.join(list(X)[::-1]) + ']')

# solution()