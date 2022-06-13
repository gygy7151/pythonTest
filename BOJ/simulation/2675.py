'''
문자열 반복
'''
for i in range(int(input())):
    R, S = map(str, input().split())
    res = ''
    S = list(S)

    for s in S:

        for j in range(int(R)):

            if s == '\\':
                res += '\\'+ s

            else:
                res += s
    
    print(res)

