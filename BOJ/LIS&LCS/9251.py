'''
LCS최장공통 부분수열
'''
def solution():
    A, B = input(), input()
    N, M = len(A), len(B)

    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

    for r in range(1, N+1):
        for c in range(1, M+1):
            if A[r-1] == B[c-1]:
                dp[r][c] = 1 + dp[r-1][c-1]
            
            else:
                dp[r][c] = max(dp[r-1][c], dp[r][c-1])
    
    return dp[-1][-1]
print(solution())


