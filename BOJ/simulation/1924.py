'''
2007년
'''
'''
두번째풀이
'''
DATE = {
    1 : 'MON',
    2 : 'TUE',
    3 : 'WED',
    4 : 'THU',
    5 : 'FRI',
    6 : 'SAT',
    7 : 'SUN'
}

def solution():
    M, D = 1, 1
    NM, ND = map(int, input().split())
    # 0이 아니라 1부터 시작해야됨
    # 날짜를 +1 씩 더하므로 시작은 월요일부터포함시켜줘야되는거임
    IDX = 1
    if (NM, ND) == (1, 1):
        print('MON')
        return
    
    while True:

        if M == 2 and D == 28:
            M += 1
            D = 1
        elif M in [1,3,5,7,8,10] and D == 31:
            M += 1
            D = 1
        elif M in [4,6,9,11] and D == 30:
            M += 1
            D = 1
        else:
            D += 1
        
        #이건 8이 아니라 7이 맞음
        #만약8이라면 이전 요일이 8일이었다는건데 말이안됨
        if IDX == 7:
            IDX = 1

        #6이면 +=1 하면 7이 되므로 7까진 포함되는거임
        else:
            IDX += 1

        if (M, D) == (NM, ND):
            break
    
    print(DATE[IDX])

solution()

'''
첫번째풀이 - 틀림 2월29일하고 3월1일하고 요일이 다름..
'''
# def solution():
#     x, y = map(int, input().split())
#     if x == 1:
#         # 아.. 여기도 str이 아니고 int타입을 파라미터값으로 넣어줘야했다.
#         return DATE[y%7]
#     total_days = y
    
#     # (실수) 1월달 요일수부터 더하고 있엇따.
#     for i in range(2,x+1):
#         total_days += MONTH[i]
#     return DATE[total_days%7]
# print(solution())
    
    



