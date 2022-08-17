'''
알고리즘수업 - 알고리즘의 수행시간 1
'''

'''
첫번째풀이
'''
def solution():
    N = int(input())

    if N == N:
        print(N//N)
        print(0)

    elif N == N**2:
        print(N//N**2)
        print(2)

    elif N == N**3:
        print(N//N**3)
        print(3)
    
    else:
        print(4)

solution()