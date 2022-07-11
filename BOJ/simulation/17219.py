'''
비밀번호찾기
'''
'''
첫번째풀이
'''
def solution():
    N, M = map(int, input().split())
    MEMO = {}
    
    for _ in range(N):
        ADDRESS, PW = map(str, input().split())
        MEMO[ADDRESS] = PW

    for _ in range(M):
        print(MEMO[input()])

solution()
