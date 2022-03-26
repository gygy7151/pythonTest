'''
돌그룹- 12886번 
'''
A, B, C = map(int, input().split())
D = A+B+C
check = [[False]*D for _ in range(D)]

def bfs():
    q = []
    q.append((A,B))
    check[A][B] = True
    while q:
        x, y = q.pop(0)
        z = D-x-y
        if x == y == z:
            print(1)
            return
        for r, k in (x,y), (x,z), (y,z):
            if r < k:
                k -= r
                r += r
            
            elif r > k:
                r -= k
                k += k
            
            else:
                continue
            c = D-r-k
            X = min(r, k, c)
            Y = max(r, k, c)
            if not check[X][Y]:
                q.append((X, Y))
                check[X][Y] = True
    print(0)
                
def solve():
    if D % 3:
        print(0)
        return
    else:
        bfs()

solve()

# from collections import deque

# def bfs():
#     q = deque()
#     q.append((A, B))
#     check[A][B] = True
#     while q:
#         x, y = q.popleft()
#         z = D-x-y
#         if x == y == z:
#             print(1)
#             return
#         for a, b in (x, y), (x, z), (y, z):
#             if a < b:
#                 b -= a
#                 a += a
#             elif a > b:
#                 a -= b
#                 b += b
#             else:
#                 continue
#             c = D-a-b
#             X = min(a, b, c)
#             Y = max(a, b, c)
#             print(X)
#             print(Y)
#             if not check[X][Y]:
#                 q.append((X, Y))
#                 check[X][Y] = True
#     print(0)

# def solve():
#     if D % 3:
#         print(0)
#         return
#     else:
#         bfs()

# A, B, C = map(int, input().split())
# D = A+B+C
# check = [[False]*D for _ in range(D)]
# solve()

# def same():
#     if A == B and B == C:
#         print(1)
#     else:
#         print(0)
    

# if A < B:
#     A += A
#     B -= A
#     same()
# elif A > B:
#     B += B
#     A -= B
#     same()
# elif B < C:
#     B += B
#     C -= B
#     same()
# elif B > C:
#     C += C
#     B -= C
#     same()
# elif C > A:
#     A += A
#     C -= A
#     same()
# elif C < A:
#     C += C
#     A -= C
#     same()
# else:
#     same()

    

