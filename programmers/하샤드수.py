'''
하샤드수
'''
'''
첫번째풀이 - str도 iterator객체다
'''
def solution(x):
    return False if x % sum([int(x) for x in str(x)]) else True