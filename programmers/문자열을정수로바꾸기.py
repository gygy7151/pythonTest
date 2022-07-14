'''
문자열을 정수로 바꾸기
'''
'''
두번째풀이 - 좀더 알고리즘 방식으로 접근
'''
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result

'''
첫번째풀이
'''
def solution(s):
    return int(s)