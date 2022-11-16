'''
구간나누기
'''
'''
세번째풀이
'''
def solution():
    N, M = map(int, input().split())
    nums = [ int(input()) for _ in range(N)]
    # i번째수 포함하는 경우
    DP1 = [[-32769 for _ in range(M+1)] for _ in range(N)]
    # i번째수 안포함하는 경우
    DP2 = [[-32769 for _ in range(M+1)] for _ in range(N)]
    DP1[0][0] = 0
    DP2[0][1] = nums[0]

    for i in range(1, N+1):
        DP1[i][0] = 0
        DP2[i][0] = -32769
        for j in range(1, min(M, (i+2)//2) + 1):
            DP1[i][j] = max(DP1[i-1][j], DP2[i-1][j])
            DP2[i][j] = max(DP1[i-1][j-1]+nums[i], DP2[i-1][j]+nums[i])
    
    print(max(DP1[N-1][M], DP2[N-1][M]))
solution()