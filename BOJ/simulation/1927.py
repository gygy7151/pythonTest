'''
최소힙
'''
'''
첫번째풀이
'''
import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())
    A = []

    for _ in range(N):

        # 파이썬 3.8 바다코끼리 연산자 the walrus operator 활용
        if num := int(input()):
            heapq.heappush(A, num)

        else:

            if len(A) >=1:
                print(heapq.heappop(A))

            else:
                print(0)

solution()