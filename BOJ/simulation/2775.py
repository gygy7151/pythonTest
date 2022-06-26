'''
부녀회장이 퇼테야
'''
def solution():
    #0층부터 시작하고 0호부터 시작
    apart = [[ x for x in range(15)]] + [[0]*15 for _ in range(14)]
    
    def iteration(k,n):
        nonlocal apart
        n_sum = 0
        
        # k-1층에 n호까지 다 더함
        for n_idx in range(n+1):
            n_sum += apart[k-1][n_idx]
        
        apart[k][n] = n_sum
        
    #각층에 호수에 몇명이 사는지 구함
    for i in range(1, 15):
        for j in range(1, 15):
            iteration(i,j)

    # K와 N은 1부터 시작
    for _ in range(int(input())):
        K, N = int(input()), int(input())
        print(apart[K][N])

solution()