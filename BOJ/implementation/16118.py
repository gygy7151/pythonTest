'''
달빛여우
'''
'''
두번째풀이 -  빠르게 갈때 느리게 갈때 를 한큐에 해결하려고 했더니 틀렸다..
다른 풀이를 참조해보니 빠르게 갈때와 느리게 갈때를 구분하여 문제를 해결한 것을 볼 수 있었다.
추가로 가중치의 /2에 값이 유실되지 않도록 애초에 그래프 가중치 입력값을 2배로 설정했더라..
'''
'''
첫번째풀이/두번째풀이
늑대 최단거리의 경우
단순 다익스트라로만 풀면 다익스트라보다 최단경로는 아니지만
더빠르게 늑대가 갈 수 있는 경우도 존재한다..
이를 위해 애초에 빠르게 가는 경우와 느리게 가는 경우를 분리해서
거리에 담아주어야 했다.
이를 위해 그래프 가중치 입력값을 2배로 설정해줘야 했다. 2로 나눴을때 값이 유실되지 않기 위해.
'''
import heapq
import sys
input = sys.stdin.readline

def solution():
    # 오솔길 경로 및 거리정보를 graph에 저장한다
    N, M = map(int, input().split())
    path = [[] for _ in range(N+1)]
    INF = int(1e9)

    for _ in range(M):
        a, b, d = map(int, input().split())
        path[a].append((b,d*2))
        path[b].append((a,d*2))
    
    def move(start):
        foxD = [INF for _ in range(N+1)]
        # wolfD[0] 빠르게 도착, wolfD[1] 느리게 도착
        wolfD = [[INF for _ in range(N+1)] for _ in range(2)]
        foxD[start], wolfD[start][start] = 0, 0 # 그래서 느리게 도착한경우 wolf[1][1] 먼저 0으로 셋팅해줌
        foxq = []
        wolfq = []
        heapq.heappush(foxq, (0, start))
        heapq.heappush(wolfq, (0, start,1))

        while foxq:
            dist, nowNode = heapq.heappop(foxq)

            if foxD[nowNode] < dist:
                continue
            
            for newNode, cost in path[nowNode]:
                newDist = dist + cost

                if newDist < foxD[newNode]:
                    foxD[newNode] = newDist
                    heapq.heappush(foxq, (newDist, newNode))
        
        while wolfq:
            dist, nowNode, depth = heapq.heappop(wolfq)

            if depth%2 == 0 and wolfD[0][nowNode] < dist:
                continue
            
            elif depth%2 == 1 and wolfD[1][nowNode] < dist:
                continue
            
            for newNode, cost in path[nowNode]:
                if depth % 2 == 1:# 느리게 도착한경우 빠르게 출발
                    newDist = dist + (cost//2)
                    if newDist < wolfD[0][newNode]:
                        wolfD[0][newNode] = newDist
                        heapq.heappush(wolfq, (newDist, newNode, depth+1))
                
                else: #빠르게 도착한경우 느리게 출발
                    newDist = dist + (cost*2)
                    if newDist < wolfD[1][newNode]:
                        wolfD[1][newNode] = newDist
                        heapq.heappush(wolfq, (newDist, newNode, depth+1))

        return [foxD, wolfD]

    
    res = move(1)
    foxMoveCost, wolfMoveCost = res[0], res[1]
    # print(foxMoveCost) 
    # print(wolfMoveCost)
    answer = 0

    for idxWood in range(2, N+1):
        if foxMoveCost[idxWood] < min(wolfMoveCost[0][idxWood], wolfMoveCost[1][idxWood]):
            answer += 1
   
    print(answer)
solution()

    
                






