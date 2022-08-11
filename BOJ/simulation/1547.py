'''
공
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    cups = [0] + [ x for x in range(1,4)]
    
    for _ in range(N):
        X, Y = map(int, input().split())
        idxOfX, idxOfY = cups.index(X), cups.index(Y)
        cups[idxOfX] = Y
        cups[idxOfY] = X
    
    print(cups[1])

solution()