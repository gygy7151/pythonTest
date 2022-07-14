'''
그대로 출력하기2
'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readlines
def solution():
    S = input()
    for s in S:
        print(s[0:len(s)-1])
solution()