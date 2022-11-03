'''
이동하기
'''
'''
첫번/세번째풀이 -  이건 꼭 다시 답 봐야된다
'''
def solution():
    N, M = map(int, input().split())
    graph = [ list(map(int, input().split())) for _ in range(N)]
    DP = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for y in range(1, N+1):
        for x in range(1, M+1):
            DP[y][x] = graph[y-1][x-1] + max(DP[y-1][x], DP[y-1][x-1], DP[y][x-1])
    
    print(DP[N][M])

solution()