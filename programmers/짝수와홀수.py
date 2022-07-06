'''
짝수와홀수
'''
'''
첫번째풀이 - 람다형 함수형풀이
'''
def solution(num):
    check = lambda x: 'Odd' if x%2 else 'Even' 
    return check(num)