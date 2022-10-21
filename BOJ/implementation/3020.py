'''
개똥벌레
'''
'''
세번째풀이 - 누적합, 이분탐색 이용
'''
from bisect import bisect_left
import sys
input = sys.stdin.readline
def soluton():
    N, H = map(int, input().split())
    pillarTop, pillarBotm = [], []
    
    for i in range(N):
        if i % 2 == 0:
            pillarBotm.append(int(input()))
        else:
            pillarTop.append(int(input()))
    
    pillarTop.sort()
    pillarBotm.sort()

    minObstacleCnt, cntMin = 200001, 0
    
    for height in range(1,H+1):
        idxTop = bisect_left(pillarTop, H+1-height)
        idxBotm = bisect_left(pillarBotm, height)
    
        cntObstacle = N - (idxTop+idxBotm)
        if minObstacleCnt > cntObstacle:
            minObstacleCnt = cntObstacle
            cntMin = 1
        
        elif minObstacleCnt == cntObstacle:
            cntMin += 1
        

    print(minObstacleCnt, cntMin)
soluton()


'''
두번째풀이 - 메모리초과 + 틀림
장애물 순서는 석순-종유석 순서임 석순은 0인덱스부터 시작 종유석은 H인덱스부터 시작
N은 동굴의 길이이고
H는 동굴의 높이임
'''
# def solution():
#     N, H = map(int, input().split())
#     INF = int(1e9)
#     pilar = [[ 0 for _ in range(N+1)] for _ in range(H+1)]
    
#     # 개똥벌레가 부셔야 하는 구간을 1로 표시해준다
#     for x in range(1,N+1):
#         size = int(input())
#         if x % 2 != 0:
#             # 석순
#             for y in range(H, H-size, -1):
#                 pilar[y].append(1)
        
#         else:
#             # 종유석
#             for y in range(1, size+1):
#                 pilar[y].append(1)
        
#     minVal, totalCnt = INF, []

#     # 각 구간별로 개똥벌레가 지나가야하는 장애물 총 수를 구한다
#     for idx in range(1, H+1):
#         sizeObstacle = len(pilar[idx])
#         totalCnt.append(sizeObstacle)
        
#         if sizeObstacle < minVal:
#             minVal = sizeObstacle

#     print(minVal, totalCnt.count(minVal)) # 장애물의 최솟값과 그러한 구간의 총 갯수를 출력.(단순 첫번째인덱스 구하는거아님)
# solution()
            

# '''
# 첫번째풀이
# 장애물 순서는 석순-종유석 순서임 석순은 0인덱스부터 시작 종유석은 H인덱스부터 시작
# N은 동굴의 길이이고
# H는 동굴의 높이임
# '''
# def solution():
#     N, H = map(int, input().split())
#     INF = int(1e9)
#     pilar = [[ 0 for _ in range(N+1)] for _ in range(H+1)]
    
#     # 개똥벌레가 부셔야 하는 구간을 1로 표시해준다
#     for x in range(1,N+1):
#         size = int(input())
#         if x % 2 != 0:
#             # 석순
#             for y in range(H, H-size, -1):
#                 pilar[y][x] = 1
        
#         else:
#             # 종유석
#             for y in range(1, size+1):
#                 pilar[y][x] = 1
        
#     totalObstackle = [0 for _ in range(H+1)]
#     totalObstackle[0] = INF
#     # 각 구간별로 개똥벌레가 지나가야하는 장애물 총 수를 구한다
#     for race in range(1,H+1):
#         for col in range(1, N+1):
#             if pilar[race][col] == 1:
#                 totalObstackle[race] += 1
#     MIN = min(totalObstackle)

#     print(MIN, totalObstackle.count(MIN)) # 장애물의 최솟값과 그러한 구간의 총 갯수를 출력.(단순 첫번째인덱스 구하는거아님)
# solution()