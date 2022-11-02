'''
이친수
'''
'''
네번째풀이
'''
def solution():
    N = int(input())
    #예외처리 DP 만들기 전에 해줘야됨 주의
    if N < 3:
        print(1)
        return
    DP = [0 for _ in range(N+1)]
    DP[1] = 1
    DP[2] = 1

    for idx in range(3, N+1):
        DP[idx] = DP[idx-1] + DP[idx-2]
    
    print(DP[N])
solution()