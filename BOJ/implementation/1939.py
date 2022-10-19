'''
중량제한
싸이클이 있네? 그래프군..
모든다리는 양방향임
공장이 있는 두섬을 연결하는 경로는 반드시 존재함
'''
'''
두번째풀이
'''
from collections import deque
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    factory = [[] for _ in range(N+1)]

    for _ in range(M):
        A, B, C = map(int, input().split())
        factory[A].append((B,C))
        factory[B].append((A,C))
    
    factoryA, factoryB = map(int, input().split())

    def bfs(weight):
        q =  deque()
        visited = set()
        q.append(factoryA)
        visited.add(factoryA)

        while q:
            islandA = q.popleft()
            for islandB, maxWeight in factory[islandA]:
                # if weight > maxWeight: -> 이러면 안됨 다른 섬들은 q에 들어갈 수 있는 길이 막히는 거임
                    # break
                
                if islandB not in visited and weight <= maxWeight:
                    visited.add(islandB)
                    q.append(islandB)

        if factoryB in visited:
            return True
        else:
            return False

        
                
    MIN, MAX = 1, 1000000000
    result = MIN
    
    # while조건문은 MIN이 MAX보다 작을때까지 였군..
    while MIN <= MAX:
        mid = (MIN + MAX) // 2

        if bfs(mid):
            result = mid
            MIN = mid + 1
        
        else:
            #MAX엔 mid-1을 대입해줬어야됨 아하..
            MAX = mid - 1
    
    print(result)

solution()









'''
첫번째풀이 - 시간초과
두개의 섬사이에 경로가 여러개이므로
각 섬사이 경로를 따로 굳이 내림차순 정렬해줄 필요없음
이분탐색이 모든걸 해결해줄꺼임
'''
# from collections import deque
# import sys
# input = sys.stdin.readline
# def solution():
#     N, M = map(int, input().split())
#     factory = [[] for _ in range(N+1)]

#     for _ in range(M):
#         A, B, C = map(int, input().split())
#         factory[A].append((B,C))
#         factory[B].append((A,C))
    
#     factoryA, factoryB = map(int, input().split())

#     def bfs(weight):
#         q =  deque()
#         visited = set()
#         q.append(factoryA)

#         while q:
#             islandA = q.popleft()
#             if islandA == factoryB:
#                 return True
#             for data in factory[islandA]:
#                 islandB, maxWeight = data
#                 if weight > maxWeight:
#                     return False
                
#                 elif islandB not in visited and weight <= maxWeight:
#                     visited.add(islandB)
#                     q.append(islandB)
        
#         return True
                
#     MIN, result = 1, 0
    
#     while MIN <= 100000:
#         if bfs(MIN):
#             result = max(MIN,result)
#             MIN += 1
    
#     print(result)

# solution()

