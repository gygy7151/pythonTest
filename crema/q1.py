'''
날짜스트링 포맷 변환 하기

[입력조건]
1.day는 1st, 2nd, 3rd, 21st, 22nd, 23rd, 31st를 제외한 나머지 숫자는 뒤에 th가 붙는다.
2.month는 약어로 Jan, Feb..형태로 값이 입력된다.
3.year는 1900부터 2100까지 4자리 숫자형태로 입력된다.

애시당초 처음 입력 받은 값


맨처음은 어떻게 해야될까?
우선 배열의 길이와
배열요소를 모두 입력받는다.


그다음

    여기서 일,월,년 요소에 접근 하고
day랑 month

for i in range(len(dates)) :
    date  = list(map(str, input(dates[i]).split()))

    day = list[]
    month = list[]
    year = list[]

    for y in range(1900, 2101) :
        if y == 
        for m in months :

            for d in days :



for date in dates:
    어떻게 변환해야 ....일은 일이고
    월은 월이고, 년은 년으로 숫자를 리턴할 수 있을까?
    들어오는 과정을 상상해보면

'''

import re


n = int(input())

months = {'Jan' : '01', 'Feb' : '02', 'Mar' : '03', 'Apr': '04', 'May' : '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}


def solution(n):
    day = ''
    month = ''
    year = ''
    result = []

    dates = [0] * n
    print(dates, '초기 빈배열')

    for i in range(n) :
        dates[i] = list(map(str, input().split()))

    print(dates, '배열 요소 추가완료')


    for i in range(n): 
        date = dates[i]
        print(date, 'dates 리스트에서 추출한 {}번째 요소'.format(i))

        for i, item in enumerate(date) :
            print(item, i)
            
            #DAY MONTH YEAR -> YYYY-MM-DD
            if i  == 0 :
                
                #list형식으로 리턴함
                nday = re.findall('\d', item)
                #print(len(nday), '숫자길이')

                if len(nday) == 1 :
                    day = '0' + ''.join(nday)
                    #print(day, '바뀐일자')

                else :
                    day = ''.join(nday)
                    #print(day, '바뀐일자')
               


            elif i  == 1 :
                month = months[date[1]]
                #print(month, '바뀐 달')

            
            elif i == 2 :
                year = date[2]
                #print(year, '바뀐 년도')
            
        ndate = year + '-' + month + '-' + day
        #(ndate, '변환된 최종일자')
        result.append(ndate)
    
    print(result)


solution(n)

