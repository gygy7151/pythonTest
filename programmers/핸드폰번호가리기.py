'''
핸드폰 번호가리기
'''
'''
첫번째풀이
'''
def solution(phone_number):
    s = phone_number
    return '*'*(len(s)-4) + s[-4:]