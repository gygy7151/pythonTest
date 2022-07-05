'''
콜라츠추측
'''
'''
첫번째풀이- answer변수사용 ,두번째풀이 - num 직접사용
'''
def solution(num):
    cnt = 0 
    if num == 1: return 0
    
    while num > 1:
        num = num/2 if num % 2 == 0 else (num*3)+1
        cnt += 1

    return cnt if num == 1 and cnt <= 500 else -1