
'''
2016년
'''
'''
세번째풀이
'''
def solution(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU','FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return days[sum(months[:a-1]+b)%7]

'''
두번째풀이- 참조코드
'''
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

'''
첫번째풀이
'''
MONTH = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

DATE = {
    0 : 'THU',
    1 : 'FRI',
    2 : 'SAT',
    3 : 'SUN',
    4 : 'MON',
    5 : 'TUE',
    6 : 'WED',
}

def solution(a, b):
    answer = ''
    if a == 1:
        return DATE[b % 7]
    
    dates = b
    for i in range(1, a):
        dates += MONTH[i]
    print(dates)
    return DATE[dates % 7]