'''
OX퀴즈
'''
for i in range(int(input())):
    answer  = 0
    prst_score = 0
    result = list(map(str, input().rstrip()))
    for res in result:
        if res == 'O':
            prst_score += 1
            answer += prst_score
        else:
            prst_score = 0
    print(answer)

