'''
LCS 2
'''
def solution():
    A, B = input(), input()
    N, M = len(A), len(B)
    ANS = ''

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for r in range(1, N+1):
        tag = True
        for c in range(1, M+1):
            # 열먼저 그리고 행 다음임
            if A[c-1] == B[r-1]:
                dp[r][c] = 1 + dp[r-1][c-1]
            
            else:
                dp[r][c] = max(dp[r-1][c], dp[r][c-1])

    now = dp[-1][-1]
    x = len(dp) - 1
    y = len(dp[0]) - 1

    while now != 0:
        if dp[x][y-1] == now -1 and now -1 == dp[x-1][y]:
            ans = A[y - 1] + ans
            now -= 1
            x -= 1
            y -= 1
        
        else:
            if dp[x -1][y] > dp[x][y-1]:
                x -= 1
            else:
                y -= 1

    print(dp[-1][-1])
    print(ans)
solution()

