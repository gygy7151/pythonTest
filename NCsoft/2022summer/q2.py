import re
def solution(birth):
    answer = 0
    for date in birth:
        if '-' not in date:
            continue
        res = date.count('-')
        if res >= 3 or len(date) == res:
            continue
        birthday = date.split('-')
        # 0:'YYYY', 1:'MM', 2:'DD'
        total_length = len(birthday[0]) + len(birthday[1]) + len(birthday[2]) + 2
        if total_length != 10:
            continue
        if len(birthday[0]) != 4 or len(birthday[1]) != 2 or len(birthday[2]) != 2:
            continue
        if 1900 <= int(birthday[0]) <= 2021:
            if 1 <= int(birthday[1]) <= 12:
                #4
                if birthday[1] in [ '01','03','05','07','08','10','12' ]:
                    if 1 <= int(birthday[2]) <= 31:
                        answer += 1
                #5
                elif birthday[1] in [ '04','06','09','11' ]:
                    if 1 <= int(birthday[2]) <= 30:
                        answer += 1
                #6
                elif int(birthday[1]) == 2:
                    if int(birthday[0]) % 400 == 0:
                        if 1 <= int(birthday[2]) <= 29:
                            answer += 1
                    elif int(birthday[0]) % 4 == 0 and int(birthday[0]) % 100 != 0:
                        if 1 <= int(birthday[2]) <= 29:
                            answer += 1
                    else:
                        if 1 <= int(birthday[2]) <= 28:
                            answer += 1
    return answer