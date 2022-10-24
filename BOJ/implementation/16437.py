'''
양 구출 작전
'''
'''
세번째풀이 - 트리 후위순회 활용해야함 - 내가 문제 푼 기여 0%
'''
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def solution():
    N = int(input())
    arr = [[], [0,0]]
    arr2 = [[] for _ in range(N+2)]
    res = 0

    for idx in range(2, N+1):
        t, a, p = input().split()
        a = int(a)
        p = int(p)
        arr.append([t, a, p])
        arr2[p].append(idx)
    
    def dfs(now):
        total = 0
        # arr2로 돌아줘야됨 arr가 아님
        for i in arr2[now]:
            total += dfs(i)
        
        if arr[now][0] == 'S' and now != 1:
            total += arr[now][1]
        
        elif arr[now][0] == 'W':
            total = total - arr[now][1]
        
        if total <= 0:
            total = 0
        
        return total

    res = dfs(1)
    print(res)
solution()

'''
첫번째/두번째풀이- 틀림 100%
'''
'''
어떻게 풀꺼냐면
먼저 각섬이 어디로 가는지 저장하고
각섬이 늑대섬인지 양섬인지 구분해야 될꺼아님?
2번부터..
'''
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 8)
# def solution():
#     N = int(input())
#     # 연결정보 담은 배열 graph i번섬에서 graph[i]번 섬으로 이동가능함 표시
#     graph = [[] for _ in range(N+1)]
#     # 늑대만 따로 개체수 정보담은 배열 woolf
#     woolf = [0 for _ in range(N+1)]
#     # 양의 개체수 및 현재 머무는 섬 정보 담은 배열 sheep
#     sheep = []

#     for idx in range(2, N+1):
#         data = list(input().split())
#         animalType, cntToLive, linkIsland = data[0], int(data[1]), int(data[2])
#         if animalType == 'S':
#             sheep.append((cntToLive, linkIsland))
#         else:
#             woolf[idx] = cntToLive

#         #번으로 가는거니깐 방향을 역으로 설정해주어야 했음?
#         graph[linkIsland].append(idx)

#     answer = 0
#     def dfs(cntSheep, nowIsland):
#         nonlocal answer
#         if woolf[nowIsland] >= cntSheep:
#             return
        
#         if nowIsland == 1:
#             # dfs로 리턴하기보단 answer 전역변수에 바로 더해주는게 좋음. -> dfs가 None을 리턴할 수있으므로.
#             return cntSheep
#         # 아 예외처리를 안했어. 늑대가 있는섬인지 아닌지 반드시 예외처리 해줘야됨
#         if woolf[nowIsland] == 0:
#             for c in graph[nowIsland]:
#                 dfs(cntSheep, c)
#         else:
#             for c in graph[nowIsland]:
#                 dfs(cntSheep-woolf[nowIsland], c)
    
#     for cntSheep, nowPos in sheep:
#         dfs(cntSheep, nowPos)
    
#     print(answer)
# solution()
