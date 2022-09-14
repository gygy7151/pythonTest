'''
카드구매하기
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    card = list(map(int, input().split()))
    card.insert(0,0)
    D = [0 for _ in range(N+1)]
    D[1] = card[1]

    if N < 2:
        print(D[1])
        return
    
    for i in range(2, N+1):
        for j in range(1, i+1):
            D[i] = max(D[i], D[i-j] + card[j]) # max비교값은 card[j]가 아님 D[i]임
    
    print(D[N])

solution()