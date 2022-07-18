'''
카잉달력
'''
'''
세번째풀이 - 최소공배수를 활용한 k번째 해구하기
x,y가 다시 등장하는 숫자를 구해보면
X는 M의배수 Y는 N의 배수인데
정답 k는 x,y가 같아 지는 즉, M,N의 최소공배수를 구하는게 목적이였다.
만약 최소공배수가 존재한다면,
x에 M을 계속 더했을때 어느순간 x % N == y 가 되는 시점이 된다.
이때 x를 리턴해주면 그 값이 k가 된다.
y가 되지않고 x가  N*M보다 값이 커졌다면
그땐 -1을 리턴하여 x,y가 유효하지 않은 값임을 알려주면 끝나는 아주 간단하고 쉬운 문제였다.
어떤 사람들은  (x - y) % N == 0으로 좀더 식을 깔끔하게 y를 제외하고 깔끔하게 나누어떨어지는
값을 조건으로 만든 사람들이 많았는데 나는 그냥 귀찮아서 y를 그대로 살렸다.
근데, 그렇게 하니깐 틀렸다고 나왔다.
x에 y를 빼고 N으로 나눈 나머지가 0이 반드시 될때에만 x를 프린트해주어야 하나보다.
왤까. 왜 y가 나오면 안될까..
아 같은 x값이 안나오게 되서 순번이 달라져서 그런가보다.
아.. 그게 아니라 y % N 이여야 했다.
y가 N보다 작으면 상관없는데 N보다 크거나 같은 경우를 고려하지 못했다.

'''
def solution():
    
    def kaing(M,N,x,y):
        while x <= M*N:
            if (x-y) % N == 0:
                print(x)
                return
            x += M
        print(-1)

    for _ in range(int(input())):
        M, N, x, y = map(int, input().split())
        kaing(M,N,x,y)

solution()

''''
첫번째/두번째풀이 - 시간초과
'''
# import sys
# input = sys.stdin.readline
# def solution():
    
#     def calculate():
#         M, N, x, y = map(int, input().split())
#         alpha, omega, order = 1, 1, 1
#         tag = 0
#         MEMO = {}
#         while alpha != M or omega != N:
#             #아..예외처리가 어려웠다. 마지막해는 x,y보다 알파와오메가가 클때가 아니였음
#             if alpha == M and omega == N:
#                 print(-1)
#                 return
#             if alpha == x and omega == y:
#                 print(order)
#                 return

#             if alpha == M:
#                 tag += 1
            
#             if tag== 3:
#                 if not MEMO[(x,y)]:
#                     print(-1)
#                     return

#             if alpha == M:
#                 alpha = 1
#             else:
#                 alpha += 1

#             if omega == N:
#                 omega = 1
            
#             else:
#                 omega += 1
            
#             order += 1
#             MEMO[(x,y)] = True
        
#         print(-1)
#         return
    
#     for _ in range(int(input())):
#         calculate()

# solution()