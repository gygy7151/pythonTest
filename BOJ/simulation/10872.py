
'''
팩토리얼
'''
def solution(N):
    ans = 1
    if N <= 1:
        return 1
    for i in range(2,N+1):
        ans += i
        print('the ans is {0}'.format(ans))
    return ans
N = 10
print(solution(N))
