'''
열개씩 끊어 출력하기
'''
'''
첫번째풀이
'''
def solution():
    S = input()
    ANS = []
    for i in range(0, len(S), 10):
        if i+10 <= len(S):
            ANS.append(S[i:i+10])
        else:
            ANS.append(S[i:])
    return ANS
res = solution()
print(*res, sep="\n")