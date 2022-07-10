'''
동전0
'''
'''
첫번째풀이
'''
def solution():
    N, K = map(int, input().split())
    COIN = []
    ANS = 0

    for _ in range(N):
        COIN.append(int(input()))
    
    COIN.sort(reverse=True)

    while True:
        num = 0

        for coin in COIN:
            if coin <= K:
                num = coin
                break

        ANS += (K // num)
        K = (K % num)
        if K <= 0:
            break
    
    return ANS
print(solution())


    