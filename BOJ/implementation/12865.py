'''
평범한 배낭 - 추후 0-1 knapsack도 풀어봐야됨
'''
'''
첫번째풀이
'''
def solution():
    N, K = map(int, input().split())
    stuff = [[0,0]]
    DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for _ in range(N):
        stuff.append(list(map(int, input().split())))

    for type in range(1, N+1):
        for newBagWg in range(1, K+1):
            nowBagWg, nowBagVal = stuff[type][0], stuff[type][1]

            #넣을 물건 무게가 현재배낭허용무게보다 더 크면 넣지 않는다.
            if newBagWg < nowBagWg:
                DP[type][newBagWg] = DP[type-1][newBagWg]
            
            else:
                DP[type][newBagWg] = max(nowBagVal + DP[type-1][newBagWg-nowBagWg], DP[type-1][newBagWg])
    
    print(DP[N][K])

solution()