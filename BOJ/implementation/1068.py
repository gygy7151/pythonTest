'''
트리
'''
'''
두번째풀이 - 아..내생각이 짧았다. target노드 하나만 생각할게 아니라 target노드를 부로갖는 노드들의 자식노드까지 제거해주어야했다.
그래서 dfs가 필요했던 것..
'''
def solution():
    n = int(input())
    tree = [[] for _ in range(n)]
    p = list(map(int, input().split()))
    for i in range(n):
        tree[i] = p[i]
    remove = int(input())

    def delete(remove):
        tree[remove] = -2
        for i in range(n):
            if tree[i] == remove:
                tree[i] = -2
                delete(i)
    delete(remove)
    cnt = 0
    for i in range(n):
        if tree[i] != -2:
            err = 0
            for j in tree:
                if j == i:
                    err = 1
                    break
            if err == 0:
                cnt += 1
    print(cnt)

solution()
'''
첫번째풀이 - 틀림
'''
# def solution():
#     N = int(input())
#     # 부모노드 정보 담긴 배열 tree
#     tree = list(map(int, input().split()))
#     M = len(tree)
#     targetNode = int(input())
#     tree[targetNode] = -2 # 모든노드는 N보다 작은 자연수 또는 0임
#     # 타겟노드가 자기자신을 부모로 가리키는 경우도 있을 수 있지만
#     # 정답을 구하는데 있어서 상관없음 어차피 -2로 초기화할꺼임 for 삭제
    
#     # 삭제된 노드 넘버를 담은 배열
#     isNotNode = []
    
#     for nodeIdx in range(M):
#         if tree[nodeIdx] == targetNode:
#             tree[nodeIdx] = -2
#             isNotNode.append(nodeIdx)
    
#     # 진입차수 담은 배열 isDegree
#     isDegree = [0 for _ in range(N)]

#     for nodeIdx in range(M):
#         if tree[nodeIdx] >= 0:
#             isDegree[tree[nodeIdx]] += 1
    
#     # 진입차수가 0인 리프노드 갯수 answer
#     answer = 0
#     for i in range(N):
#         if isDegree[i] == 0:
#             if i not in isNotNode:
#                 answer += 1
    
#     print(answer-1) # 부모노드는 갯수에서 제외한다 -1

# solution()





    
    


