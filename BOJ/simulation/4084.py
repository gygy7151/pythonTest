'''

'''
'''
첫번째풀이
'''
import sys
input = sys.stdin.readline

def solution():
    
    while True:
        A, B, C, D = map(int, input().split())
        if (A + B + C + D) == 0:
            return
        answer = 0
        while A != B or B != C or C != D:
            answer += 1
            tempA, tempB, tempC, tempD = abs(A-B), abs(B-C), abs(C-D), abs(D-A)
            A, B, C, D = tempA, tempB, tempC, tempD

        print(answer)
        
solution()

