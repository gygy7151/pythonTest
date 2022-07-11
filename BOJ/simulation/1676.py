'''
팩토리얼 0의개수
'''
'''
두번째 풀이 - 틀림: 0! == 1인데 0이라고 잘못 판단하여 0의 갯수를 1개로 정답이 아닌 값을 리턴함.
'''
'''
첫번째풀이 - 틀림 : 맨처음 0이 아닌 숫자가 나오면 예외처리 해주어야 하는데 그러질 못햇음
'''
def solution():
    ANS = 0
    N = int(input())
    if N == 0:
        return 0

    def factorial(n):
        RES = 1
        for i in range(1,n+1):
            RES *= i
        return RES
    

    N = factorial(N)
    # print(str(N)[::-1])

    for digit in str(N)[::-1]:
        if digit == '0':
            ANS += 1
        else:
            break

    return ANS
print(solution())
