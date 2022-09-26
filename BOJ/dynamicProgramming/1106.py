'''
호텔
'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readline
def solution():
    C, N = map(int, input().split())
    data = [map(int, input().split()) for _ in range(N)]
    # 초기값을 무한대, 즉 제일 큰값으로 안해주었다.
    INF = int(1e9)
    dp = [ INF for _ in range(C+100)]
    dp[0] = 0

    for cost, cust_cnt in data:
        for i in range(cust_cnt, C + 100):
            dp[i] = min(dp[i], dp[i-cust_cnt] + cost)
    
    print(min(dp[C:]))

solution()
