'''
x만큼 간격이 있는 n개의 숫자
'''
'''
첫번째풀이
'''
def solution():
    x,n = map(int, input().split())
    if x == 0: return [0]*n
    return [ x for x in range(x, x*n+1 if x >0 else x*n-1, x)]