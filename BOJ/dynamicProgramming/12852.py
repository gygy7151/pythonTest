'''
1로 만들기 2
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    dp = [[0, 0] for _ in range(N+1)] 
    # 0번째: 연산횟수 최솟값(단 3가지연산비교) 
    # #1번째:(0번째 최솟값 만든 인덱스 즉, 몫을 값으로 채우면됨)
    dp[1][0] = 0 # 자기자신을 또 만드는방법은 없음
    dp[1][1] = 0 # 1은 자기자신이니깐

    for i in range(2, N+1):
        dp[i][0] = dp[i-1][0] + 1
        dp[i][1] = i - 1
        if i % 3 == 0 and dp[i//3][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i//3][0] + 1
            dp[i][1] = i//3

        if i % 2 == 0 and dp[i//2][0] + 1 < dp[i][0]:
            dp[i][0] = dp[i//2][0] + 1
            dp[i][1] = i//2
    
    # N을 1로 만드는 연산횟수 최솟값
    print(dp[N][0])
    root = []
    start = N
    while start != 0:
        root.append(start)
        start = dp[start][1]
    
    print(*root)        

solution()

