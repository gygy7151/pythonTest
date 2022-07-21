'''
피보나치수4
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    MEMO = [ i for i in range(N+1)]

    for i in range(2,N+1):
        MEMO[i] = MEMO[i-1] + MEMO[i-2]

    return MEMO[N]
print(solution())
