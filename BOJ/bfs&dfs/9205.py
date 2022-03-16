'''
맥주마시면서 걸어가기 - 9205번
'''

def bfs(x, y):
    q, c = [], []
    q.append([x, y, 20])
    c.append([x, y, 20])
    while q:
        x, y, beer = q.pop(0)
        if x == x1 and y == y1:
            print("happy")
            return
        for nx, ny in d:
            #방문처리를 해줘야 무한루프지옥에서 벗어난다.안그럼 무한대로 q에 값이 들어감 주의.
            if [nx, ny, 20] not in c:
                l1 = abs(nx - x) + abs(ny - y)
                if beer*50 >= l1:
                    q.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return

tc = int(input())
while tc:
    n = int(input())
    x0, y0 = map(int, input().split())
    d = []
    for _ in range(n):
        x, y = map(int, input().split())
        d.append([x, y])
    x1, y1 = map(int, input().split())
    d.append([x1, y1])
    bfs(x0, y0)
    tc -= 1


# def test_case():
#     cnt = int(input())
#     x, y  = map(int, input().split())
#     pos = []
#     for _ in range(cnt+1):
#         r, k = map(int, input().split())
#         pos.append((r,k))
#     emoji = 'happy'
#     while cnt > 0:
#         for p in pos:
#             nx = p[0]
#             ny = p[1]
#             md = (((nx-x) + (ny-y)) // 50)
#             if md <= 20:
#                 if nx == pos[-1][0] and ny == pos[-1][1]:
#                     print(emoji)
#                     return
#                 continue
#             else:
#                 emoji = 'sad'
#                 print(emoji)
#                 return
#         cnt-= 1
#     x = nx
#     y = ny
            

# T = int(input())
# for _ in range(T):
#     test_case()

