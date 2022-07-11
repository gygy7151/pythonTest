'''
피보나치 함수
'''
'''
첫번째풀이
'''
def solution():
    DP = [{0:1, 1:0} for _ in range(41)]
    DP[1] = {0:0, 1:1}
    DP[2] = {0:1, 1:1}
    ANS = []

    for _ in range(int(input())):
        N = int(input())

        for i in range(3,N+1):
            DP[i][0] = DP[i-1][0] + DP[i-2][0]
            DP[i][1] = DP[i-1][1] + DP[i-2][1]
        
        ANS.append(str(DP[N][0]) + ' ' + str(DP[N][1]) )
    return ANS

res = solution()
print(*res, sep='\n')