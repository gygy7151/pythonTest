'''
그대로 출력하기
sys사용 비추
'''
def solution():
    
    ANS = []    
    while True:
        try:
            S = input()

        except EOFError:
            return ANS
        ANS.append(str(S))

res = solution()
print(*res, sep='\n')
