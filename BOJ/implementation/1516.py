'''
게임 개발
'''
'''
두번째풀이
만약 1번 건물은 선수로 2,3번이 필수라면
2번 건물하고 3번건물 시간이 서로 다른데 더 많이 걸리는 시간으로 더해주어야됨
'''
import sys
from collections import deque
input = sys.stdin.readline
# 각 건물마다 걸리는 최소시간을 구해준다
def solution():
    N = int(input())
    prevBuildingInfo = [[] for _ in range(N+1)]
    inDegree = [0 for _ in range(N+1)]
    costToBuild = [0 for _ in range(N+1)]

    for nowBuildNum in range(1, N+1):
        datas = list(map(int, input().split()))[:-1]
        costToBuild[nowBuildNum] = datas[0]
        buildingData = datas[1:]

        for prevBuildNum in buildingData:
            # 진출노드 정보를 각 노드벼롤 담아주어야했음
            prevBuildingInfo[prevBuildNum].append(nowBuildNum)
            #여기서 진입차수 각각 따로 따로 구해주어야됨
            inDegree[nowBuildNum] += 1
        

    result = [0 for _ in range(N+1)]
    q = deque()

    for i in range(1, N+1):
        # 여기서 문제였구만
        if inDegree[i] == 0:
            q.append(i)
    
    
    while q:
        now = q.popleft()
        result[now] += costToBuild[now]

        for next in prevBuildingInfo[now]:
            inDegree[next] -= 1
            result[next] = max(result[now], result[next]) # 미리 큐에넣기전에 비교해주어야했음
            if inDegree[next] == 0:
                q.append(next)
    
    print(*result[1:], sep="\n")

solution()

# import sys
# from collections import deque

# input = sys.stdin.readline
# N = int(input())

# # 노드와 간선의 정보 저장한다고 생각하면 됨
# building = [[] for _ in range(N + 1)]
# # 각 노드의 진입차수 저장
# indegree = [0] * (N + 1)
# # 건물 짓는데 걸리는 시간
# cost = [0] * (N + 1)

# for i in range(1, N + 1):
#     data = list(map(int, input().split()))[:-1]
#     cost[i] = data[0]
#     building_data = data[1:]

#     # 간선 연결 및 진입차수 설정
#     for j in building_data:
#         building[j].append(i)
#         indegree[i] += 1


# # 위상 정렬 함수
# def topology_sort():
#     result = [0] * (N + 1)
#     q = deque()

#     for i in range(1, N + 1):
#         if indegree[i] == 0:
#             q.append(i)

#     while q:
#         now = q.popleft()
#         # 큐에서 꺼낸 노드 번호에 해당하는 건물을 짓는데 걸리는 시간 저장
#         # 선수 건물 짓는데 걸리는 시간이 포함되어 있음!
#         # 즉, '선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간'이 저장됨
#         result[now] += cost[now]
#         for b in building[now]:
#             indegree[b] -= 1
#             # b번호 건물을 짓기 전에 먼저 지어야하는 선수 건물 짓는데 걸리는 시간으로 갱신
#             result[b] = max(result[b], result[now])
#             if indegree[b] == 0:
#                 q.append(b)

#     return result


# answer = topology_sort()
# for i in range(1, N + 1):
#     print(answer[i])




    




'''
첫번째풀이 - 틀림
'''

# 종족별 균형과 전체 게임시간을 조절하는 부분이 남음
# 모든 건물을 짓는데 걸리는 최소 시간을 게임플레이 시간에 근사하기로 함
# 어떤 건물을 짓기 위해선 다른 건물을 먼저 지어야 함 -> 위상정렬 스맬이 남..
# 자원은 무한히 있다고 함
# N은 건물의 종류수. 각건물을 짓는데 걸리는 시간과 앞서 있어야하는 건물번호가 주어짐
# 모든건물은 짓는 것이 가능한 입력만 주어진다고 함
# N개의 각 건물이 완성되기 까지 걸리는 최소시간을 구하셈
# from collections import deque
# def solution():
#     # 건물 종류의 수 N
#     N = int(input())
#     inDegree = [0 for _ in range(N+1)]
#     cost = [0 for _ in range(N+1)]
#     link = [[] for _ in range(N+1)]
#     q = deque()
    
#     #진입차수를 채워준다
#     for idx in range(1,N+1):
#         datas = list(map(int, input().split()))
#         costBuild = datas[0]
#         cost[idx] = costBuild
#         firstToBuildList = datas[1:len(datas)-1]
#         cntIndegree = len(firstToBuildList)
#         inDegree[idx] = cntIndegree

#         if cntIndegree == 0:
#             q.append((1, idx))
        
#         # 현재 빌딩에서 다음 빌딩과 연결된 정보를 저장
#         for building in firstToBuildList:
#             link[building].append(idx)
    
#     print(cost)
    
#     # 위상정렬을 구하고
#     vertex = [[] for _ in range(N+1)]
#     while q:
#         order, presentBuilding = q.popleft()
#         vertex[order-1].append(presentBuilding)

#         for nextBuilding in link[presentBuilding]:
#             inDegree[nextBuilding] -= 1
#             if inDegree[nextBuilding] == 0:
#                 q.append((order+1, nextBuilding))

    
#     print(link)
#     print(vertex)
#     # 1번부터 N번까지의 돌면서 N개의 각건물이 완성되는데 걸리는 최소시간을 구한다
#     # 아.. 어떤거는 이전에 구해놓은 값들을 누적으로 더해주어야 된다
#     # 진입차수별로 누적해서 구해주면 끝!
#     minValToBuilding = [0 for _ in range(N+1)]
    
#     tempSum =0
#     for idx in range(N):
#         if vertex[idx]:
#             for building in vertex[idx]:
#                 tempSum += cost[building]
            
        
#         print(tempSum)
        



# solution()