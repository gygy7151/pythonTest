'''
동전2
'''
'''
세번째풀이 - 불가능한 경우에 대한 예외처리를 추가함 나머지가 0이되냐 안되냐로 판단함
'''
def solution():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    DP = [10001 for _ in range(K+1)]
    DP[0] = 0

    for coin in coins:
        for idx in range(coin, K+1):
            DP[idx] = min(DP[idx], DP[idx-coin]+1)
    

    if DP[K] == 10001:
        print(-1)
    else:
        print(DP[K])

solution()