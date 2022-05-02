
'''
퇴사 - 정답 45
'''
'''
두번째풀이 - 동적계획법 dp활용
'''
import sys
input = sys.stdin.readline
N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

d = [0] * (N+1)
for i in range(N-1, -1, -1):
    if i + T[i] > N:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], P[i] + d[i + T[i]])

print(d[0])
'''
첫번째풀이 - 틀림
'''
# N = int(input())
# table = [(0,0)]
# for _ in range(N):
#     a, b = map(int, input().split())
#     table.append((a,b))
# max_profit = 0
# for j in range(1, N+1):
#     profit = 0
#     temp = [1] * (N+1)
#     for k in range(j,0, -1):
#         if table[k][1] == 1:
#             profit += table[k][1]
#     for i in range(j,N+1):
#         if temp[i] == 1:
#             day = table[i][0]
#             profit += table[i][1]
#             if j == N and day != 1:
#                 continue
#             for d in range(day):
#                 if i+d < N+1:
#                     temp[i+d] = 0
#     max_profit = max(max_profit, profit)

# print(max_profit)

    

