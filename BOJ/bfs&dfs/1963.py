'''
소수경로
'''
'''
세번째풀이
'''
from collections import deque
import sys
input = sys.stdin.readline

# 소수 전처리
def solution():
    memo = [True for i in range(10001)]
    for i in range(2, int(10000**(0.5))):
        if memo[i]:
            j = i * 2
            while j < 10001:
                memo[j] = False
                j += i

    # 일의자리수부터 십, 백, 천의자리수 까지 숫자 바꾸면서 소수구하기
    def bfs(a,b):
        q = deque()
        q.append(a)
        visit = [-1 for i in range(10000)]
        visit[a] = 0
        while q:
            num = q.popleft()
            if num == b: return visit[num]
            if num < 1000: continue
            
            # 일,십,백,천의 자리를 0으로 초기화시켜주고 크으..내가 너비 우선 범위를 잘못 선정했음.
            for i in [1, 10, 100, 1000]:
                n = num - num % ( i * 10) // i * i
                
                for j in range(10):
                    if visit[n] == -1 and memo[n]: # visit은 방문하지 않은 용도를 찾는기능임 헷갈리지말것
                        visit[n] = visit[num]+ 1
                        q.append(n)
                    n += i 

    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(bfs(a,b))

solution()
'''
두번째풀이
'''
# from collections import deque

# def solution():
#     MAX = 10000
#     memo = [1] * 10001
#     memo[0] = memo[1] = 0

#     for i in range(2, int(MAX**(0.5))):
#         if memo[i]:
#             for j in range(2*i, MAX, i):
#                 memo[j] = 0
    

#     def bfs():
#         q = deque()
#         q.append(a)
#         visit[a] = 0
        
        
            

#     for i in range(int(input())):
#         a, b = map(int, input().split())
#         visit = [-1] * 10000
#         print(bfs())

# solution()


'''
첫번째풀이 -  틀림
'''
# from collections import deque
# def solution():
#     MAX = 10 ** 4
#     memo = [1 for _ in range(MAX+1)]
#     memo[0] = memo[1] = 0

#     for i in range(2, int(MAX ** 0.5) + 1):
#         if not memo[i]:
#             continue

#         for j in range(i * i, MAX, i):
#             memo[j] = 0
    
#     def bfs(a, b):
#         q = deque()
#         visited = [-1] * MAX

#         q.append(a)
#         visited[a] = 0

#         while q:
#             num = q.popleft()

#             if num == b:
#                 return visited[num]

#             # 천의자리
#             for i in range(1, 10):
#                 new = i * 1000 + num % 1000

#                 if str(new)[0] != '0':
#                     if memo[new] and visited[num] == -1:
#                         q.append(new)
#                         visited[new] = visited[num] + 1
            
#             # 백의 자리
#             for i in range(10):
#                 new = num // 1000 * 1000 + i * 100 + num % 100
#                 if str(new)[0] != '0':
#                     if memo[new] and visited[num] == -1:
#                         q.append(new)
#                         visited[new] = visited[num] + 1

#             # 십의 자리
#             for i in range(10):
#                 new = num // 100 * 100 + i * 10 + num % 10
#                 if str(new)[0] != '0':
#                     if memo[new] and visited[num] == -1:
#                         q.append(new)
#                         visited[new] = visited[num] + 1

#             # 일의 자리
#             for i in range(10):
#                 new = num // 10 * 10 + i
#                 if str(new)[0] != '0':
#                     if memo[new] and visited[num] == -1:
#                         q.append(new)
#                         visited[new] = visited[num] + 1

#         return "Impossible"

#     for _ in range((int(input()))):
#         a, b = map(int, input().split())

#         print(bfs(a, b))

# solution()


