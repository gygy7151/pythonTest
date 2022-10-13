'''
사다리조작
'''



'''
두번째풀이 - 아.. 나는 세로선만 체크하면 되었는데 가로선까지 체크해주었다.
정확히는 사전에 미리 만들 수 있는 사다리 위치를 구해준 다음 dfs를 돌렸다.
백트래킹으로 가로선 하나 만들고 i번 세로선의 결과가 i번이 나오는지 체크한다.
그리고 그래프 상태값은 visited로 방문처리용도로 활용한 아이디어가 돋보였다.
나중에 나도 이렇게 활용하면 될듯. - 그래도 시간초과남
'''
def solution():
    N, M, H = map(int, input().split())
    ans = 0
    # 아.. H가 y였음 깜빡함
    visited = [[0 for _ in range(N+1)] for _ in range(H+1)]

    for _ in range(M):
        a, b = map(int, input().split()) #a는 세로선임.
        visited[a][b] = 1
    

    def check(visited):
        for i in range(1, N):
            now = i
            for j in range(1, H+1):
                if visited[j][now -1]:
                    now -= 1
                
                elif visited[j][now]:
                    now += 1
            
            if now != i:
                return False
        
        return True
    
    answer = 4

    def dfs(cnt, visit, x, y): #추가한 가로선 개수 cnt
        nonlocal ans

        if cnt >= ans:
            return
        
        if check(visit):
            ans = min(cnt, ans)
            return

        if cnt == 3:
            return
        
        # 후보군을 점차 줄이는 기법이라고 보면됨
        for i in range(x, H+1):
            if x == i:
                k = y
            else:
                k = 0
            
            for j in range(k,N):

                if not visit[i][j] and not visit[i][j-1] and not visit[i][j+1]:
                    visit[i][j] = 1
                    #추가된 자표를 다음 함수로 보냄
                    dfs(cnt+1, visit, i, j+2)
                    # 바로 직전 dfs가 다 돌고나서 다른 dfs에선 또다른 사다리를 놓을 수 있기 때문에 False로 초기화 해주어야됨
                    # 이전 dfs에선 놓을 수 있었어도 현재에선 사다리 놓을 수 없을 수도 있으므로 재귀를 구현해줌
                    visit[i][j] = 0

    
    dfs(0,visited, 1,1)

    if answer < 4:
        print(answer)
    
    else:
        print(-1)
        
solution()

'''
첫번째풀이
'''
# def solution():
#     N, M, H = map(int, input().split())
#     G = [[0 for _ in range(H+1)] for _ in range(N+1)]

#     for _ in range(M):
#         a, b = map(int, input().split())
#         G[a][b] = 1
    
#     def check(i):
#         # i번째세로선 결과가 i번이 나오도록 체크한다.
#         y, x = 1, i
        
#         while y < N+1:
#             if G[y][x] == 1:
#                 x += 1

#             elif G[y][x-1] == 1:
#                 x -= 1
            
#             y += 1
        
#         if x != i:
#             return False
#         else:
#             return True

#     add = 0
#     impossible = False
#     for i in range(1, N+1):
        
#         if check(i):
#             continue
        
#         y, x = 1, i
#         while check(i) and add < 4:       
#             #x가 i랑 같아질때까지 길 추가
#             if G[y][x-1] == 0 and G[y][x+1] == 0:
#                 G[y][x] = 1
#                 add += 1
        
#         # 하나라도 불가능한 경우이면 -1을 출력한다
#         if not check(i):
#             print(-1)
#             return
        
#         if add >= 4:
#             print(-1)
#             return
    
#     print(add)

# solution()