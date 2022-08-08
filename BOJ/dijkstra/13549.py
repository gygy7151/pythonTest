'''
숨바꼭질3
'''
'''
두번째풀이
'''
from collections import deque

def solution():
    max = 100001
    check = [False for _ in range(max+1)]
    d = [-1 for _ in range(max+1)]

    N, K = map(int, input().split())
    Q = deque()
    Q.append(N)
    #자기자신은 시작점이므로 이미 방문처리 해주어야됨 주의!
    check[N] = True
    #자기자신으로 가는 방법은 당연히 시간 가중치가 0이 되어야 함
    d[N] = 0

    while Q:
        now = Q.popleft()

        if now*2 <= max and check[now*2] == False: #순간이동
            Q.appendleft(now*2)
            check[now*2] = True
            #순간이동의 경우 +0초이므로 그대로 대입함
            d[now*2] = d[now]
        
        if now + 1 <= max and check[now+1] == False:
            Q.append(now+1)
            check[now+1] = True
            d[now+1] = d[now] + 1

        # 반대로 0보단 크거나 같아야됨 0 <= K <= 10만이기 때문에
        if now -1 >= 0 and check[now-1] == False:
            Q.append(now-1)
            check[now-1] = True
            #아..걷기는 항상 +1초임
            d[now-1] = d[now] + 1

    print(d[K])

solution()




'''
첫번째풀이 - 틀림
'''
# from collections import deque
# def solution():
#     N, K = 5, 17

#     if N == K:
#         return 0

#     def bfs():
#         q = deque()
#         depth, t_cost = int(1e9), int(1e9)
#         q.append((N,0,0))

#         while q:
#             now, cost, dpth = q.popleft()

#             if now == K:
#                 depth = min(depth, dpth)
#                 t_cost = min(t_cost, cost)
#                 continue

#             if dpth + 1 < depth:
#                 q.append((now*2, cost, dpth+1))
#                 q.append((now-1, cost+1, dpth+1))
#                 q.append((now+1, cost+1, dpth+1))
#         else:
#             print(t_cost)
    
#     bfs()

# solution()