'''
문자열내p와y의개수
'''
'''
첫번째풀이/ 변수를 선언하지않고도 가능함
'''
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
    