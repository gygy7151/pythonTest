'''
무한수열
'''
'''
두번째풀이 - N이 너무 커지면 dp테이블에 담지 못함 그래서 리스트대신 defaultdict로 담음
defaultdict을 활용하면 해당키 값이 없으면 0을 리턴해준다
'''
from collections import defaultdict
def solution():
    N, P, Q = list(map(int, input().split()))
    dp = defaultdict(int)
    dp[0] = 1

    def dfs(n):
        if dp[n] != 0:
            return dp[n]

        dp[n] = dfs(n//P) + dfs(n//Q)
        return dp[n]

    print(dfs(N))
solution()


'''
첫번째풀이 - 메모리초과
'''
# def solution():
#     N, P, Q = list(map(int, input().split()))
#     dp = [1]

#     for i in range(1, N+1):
#         num = dp[i//P] + dp[i//Q]
#         dp.append(num)
    
#     print(dp[N])
# solution()