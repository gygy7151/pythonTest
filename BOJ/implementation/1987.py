'''
알파벳
'''
'''
다섯번/여섯번째풀이
'''
import sys
input = sys.stdin.readline
def solution():
    R, C = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range(R)]
    chk = set()
    chk.add(matrix[0][0])
    answer = 1
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    def dfs(y, x, ans):
        nonlocal answer
        answer = max(ans, answer)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and not matrix[ny][nx] in chk:
                chk.add(matrix[ny][nx])
                dfs(ny, nx, ans+1)
                chk.remove(matrix[ny][nx])

    dfs(0,0,1)
    print(answer)
solution()

'''
첫번째/두번째풀이- dfs 새로 돌리기전에 갯수를 갱신해준다.
'''
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)

# def solution():
#     R, C = map(int, input().split())
#     graph = [list(input()) for _ in range(R)]
#     maxPassCnt = -1 # 시작칸도 포함
#     visited = set()
#     visited.add(graph[0][0])
    
#     def dfs(y, x, cnt):
#         nonlocal visited
#         nonlocal maxPassCnt
#         maxPassCnt = max(maxPassCnt, cnt)
        
#         for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
#             ny, nx = y + dy, x + dx
#             if 0 <= ny < R and 0 <= nx < C:
#                 if graph[ny][nx] not in visited:
#                     visited.add(graph[ny][nx])
#                     dfs(ny, nx, cnt+1)
        
#         #아..재귀라서 다시 지워주야되는구나
#         visited.remove(graph[y][x])


#     dfs(0,0, 1)
#     print(maxPassCnt)
# solution()




