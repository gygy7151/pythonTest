'''
빠른 A + B - sys.stdin.readline 활용 좋은 예제
'''
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a+b)