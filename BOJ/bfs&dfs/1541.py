'''
잃어버린 괄호
'''
'''
첫번째풀이 - re를 활용하고
'''
import re
def solution():
    s = input()
    S = [ int(x) for x in re.split('[^0-9]', s) if x ]
    O = ['+'] + [ x for x in re.split('[0-9]', s) if x]

    ss = ''
    res = 0
    for idx in range(len(S)):
        if O[idx] == '+':
            res += S[idx]
        else:
            ss += str(res) + '-'
            res = S[idx]
    #마지막으로 남은거까지 더해줘야됨
    ss += str(res)
    
    SS = [ int(x) for x in re.split( '[^0-9]' , ss) if x ]
    # 항상 맨앞은 그냥 숫자로 시작하므로 임의로 인덱스를 맞추기위함
    OO = ['+'] + [ x for x in re.split( '[0-9]', ss) if x ] 

    ANS = 0
    for idx in range(len(SS)):
        if OO[idx] == '+':
            ANS += SS[idx]
        else:
            ANS -= SS[idx]
    
    print(ANS)

solution()

# t = input()
# 대문자아닌요소들로 구분자하기, 
# T = [ x for x in re.split('[^A-Z]', t) if x]
# TT = [ x for x in re.split('[^a-z]', t) if x]
# print(T)
# print(TT)