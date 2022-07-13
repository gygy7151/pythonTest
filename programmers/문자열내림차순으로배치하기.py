'''
문자열내림차순으로배치하기
'''
'''
첫번째풀이
'''
def solution(s):
    return ''.join(sorted(list(s), reverse=True))
    