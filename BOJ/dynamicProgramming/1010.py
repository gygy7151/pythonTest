'''
다리놓기
'''
'''
두번째풀이 - dp 범위 30 30으로 제한
'''
def solution():
    #행 인덱스라기 보단 dp[n-1][m-1]안하기 위해서 행과 열을 각각 하나씩 더 추가함
    dp = [[1 for _ in range(31)] for _ in range(31)]

    #1번째행 초기화
    for i in range(31):
        dp[1][i] = i
    
    # 굳이 조건문 안걸어도 for문자체에서 걸림
    for i in range(2, 31):
        for j in range(i + 1, 31):
            dp[i][j] =  dp[i][j - 1] + dp[i - 1][j - 1]

    
    for _ in range(int(input())):
        n, m = map(int, input().split())
        print(dp[n][m])

solution()


'''
첫번째풀이- 틀림
'''
# def solution():
#     def match(n, m):
#         dp = [[0 for _ in range(m)] for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 if i == 0:
#                     dp[i][j] == 'x'
#                     continue

#                 if i > j:
#                     continue

#                 if i == j:
#                     dp[i][j] = 1

#                 elif i < j:
#                     dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
#         print(dp)
#         print(dp[n-1][m-1])
    
#     for _ in range(int(input())):
#         N, M = map(int, input().split())
#         match(N, M)
# solution()
