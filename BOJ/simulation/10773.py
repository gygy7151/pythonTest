'''
제로
'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readline
def solution():
    K = int(input())
    N = []

    for k in range(K):
        n = int(input())
        if n == 0:
            N.pop()
            continue
        N.append(n)
    return sum(N)

print(solution())

        