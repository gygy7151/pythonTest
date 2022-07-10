'''
팩토리얼 0의개수
'''
'''
첫번째풀이 - 틀림
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
