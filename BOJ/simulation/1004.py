'''
어린왕자
'''
'''
두번째풀이
'''
# T = int(input())
# for _ in range(T):
#     # 출발점 도착점
#     x1, y1, x2, y2 = list(map(int, input().split()))
#     # 행성계의 개수
#     n = int(input())
#     count = 0
#     for _ in range(n):
#         cx, cy, cr = map(int, input().split())
#         dis1 = (x1 - cx)**2 + (y1 - cy)**2
#         dis2 = (x2 - cx)**2 + (y2 - cy)**2
#         pow_cr = cr**2
        
#         if pow_cr > dis1 and pow_cr > dis2:
#             pass
#         elif pow_cr > dis1:
#             count += 1
#         elif pow_cr > dis2:
#             count += 1
            
#     print(count)
'''
첫번째풀이
'''
def solution():
    T = int(input())
    for _ in range(T):
        #아..x1,y1이거 변수 할당을 잘못했다. 그리고 4개이상의 변수는 list로 감싸서 변수할당해줘야됨
        x1, y1, x2, y2 = list(map(int, input().split()))
        N = int(input())
        answer = 0
        
        for _ in range(N):
            cx, cy, cr = map(int, input().split())
            dx1 = (x1 - cx)**2 + (y1 - cy)**2
            dx2 = (x2 - cx)**2 + (y2 - cy)**2
            r = cr**2
            if r > dx1 and r > dx2:
                continue
            elif r > dx1:
                answer += 1
            elif r > dx2:
                answer += 1
        print(answer)

solution()