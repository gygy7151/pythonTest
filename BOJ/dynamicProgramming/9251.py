'''
LCS
'''
X, Y = input(), input()
X, Y =  '0'+X, '0'+Y
N, M = len(X), len(Y)
DP = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N):
    for j in range(1, M):
        if X[i] == Y[j]:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print(DP[N-1][M-1])