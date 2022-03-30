'''
카펫 - 완전탐색
'''
def solution(brown, yellow):
    sum = brown + yellow
    for b in range(1, sum+1):
        a = sum // b
        if (sum / b) % 1 == 0:
            if (2*a + 2*b) == brown + 4:
                if a <= b:
                    return [b, a]
                else:
                    return [a, b]