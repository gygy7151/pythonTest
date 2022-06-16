'''
팰린드롬
'''
while True:
    num = list(input())
    if num[0] == '0':
        break
    re_num = num[-1::-1]
    N = len(num)
    answer = 'yes'
    for i in range(N):
        if num[i] != re_num[i]:
            answer = 'no'
            break
    print(answer)