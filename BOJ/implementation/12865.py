'''
평범한 배낭 - 추후 0-1 knapsack도 풀어봐야됨
'''
'''
첫번째풀이- 이전무게에서 빼주고 더하는건 비슷했는데 현재무게랑 이전무게를 활용하는 냅색알고리즘을 몰라서 틀렸음
다시 한번더 기억하면 좋을 듯
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
            #넣을 물건 무게가 현재배낭허용무게보다 작으면 현재 넣을 무게를 넣은 가치랑 넣을 무게를 뺀 이전 가치더한거랑, 직전에 해당 무게 가치랑 비교하면 됨.
            else:
                DP[type][newBagWg] = max(nowBagVal + DP[type-1][newBagWg-nowBagWg], DP[type-1][newBagWg])
    
    print(DP[N][K])

solution()