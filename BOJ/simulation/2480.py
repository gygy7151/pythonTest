'''
주사위 세개
'''
A, B, C = map(int, input().split())
res = 0
if 1 <= A < 7 and 1 <= B < 7 and 1<= C < 7:
    #같은눈3개
    if A == B and B == C:
        res = 10000 + (A * 1000)
        print(res)
    #같은눈2개
    elif A != B and B == C or A == B and B != C:
        res = 1000 + (B * 100)
        print(res)
    elif A == C and B != A and B != C:
        res = 1000 + (A * 100)
        print(res)
    #모두다른경우
    else:
        temp = sorted([A,B,C], reverse=True)
        res = temp[0] * 100
        print(res)