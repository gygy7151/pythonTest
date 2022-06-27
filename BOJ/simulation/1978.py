'''
소수찾기
'''
def solution():
    N = int(input())
    DATA = list(map(int, input().split()))
    MEMO = [0,0] + [1]* 1000

    #소수표시
    for i in range(2,41):
        for j in range(i*2,1001,i):
            if MEMO[j] == 1:
                MEMO[j] = 0

    answer = 0
    for num in DATA:
        if MEMO[num] == 1:
            answer += 1

    return answer
print(solution())

    
    


