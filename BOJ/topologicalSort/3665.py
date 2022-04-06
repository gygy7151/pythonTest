'''
최종순위 - 3665번
'''
for _ in range(int(input())):
    n = int(input())
    rank = list(map(int, input().split()))
    indegree = [-1] + [0] * n
    temp = [[] for _ in range(n+1)]
    #작년순위
    for i in range(n):
        temp[rank[i]] = rank[i+1:]
        indegree[rank[i]] = i
    
    #순위역전
    for _ in range(int(input())):
        a, b = map(int, input().split())
        #b는 a로 갈 수 있다. -> b는 a로 갈 수 없다.(remove)
        #a는 b로 갈 수 없다. -> a는 b로 갈 수 있다.(append)
        if b in temp[a]:
            temp[a].remove(b)
            temp[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
        #b는 a로 갈 수 없다. -> b는 a로 갈 수 있다.(append)
        #a는 b로 갈 수 있다. -> a는 b로 갈 수 없다.(remove)
        else:
            temp[a].append(b)
            temp[b].remove(a)
            indegree[b] += 1
            indegree[a] -= 1
    
    # 시작노드
    q = []
    for i in range(1, n+1):
        #indegree[i]가 0이면
        if not indegree[i]:
            q.append(i)
    if not q:
        #시작노드 부재, 사이클
        print('IMPOSSIBLE')
        continue
    
    #위상정렬
    ans = []
    while q:
        v = q.pop(0)
        ans.append(v)
        for i in temp[v]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
    if sum(indegree) > -1:
        print('IMPOSSIBLE')

    else:
        print(*ans)








