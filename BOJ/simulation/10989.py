'''
수 정렬하기 3
'''
import sys
def solution():
    input = sys.stdin.readline
    N = [0] * 10001
    for _ in range(int(input().rstrip())):
        N[int(input().rstrip())] += 1

    for i in range(10001):
        if N[i] == 0:
            continue
        for _ in range(N[i]):
            print(i)
solution()