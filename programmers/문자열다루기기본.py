'''
문자열다루기기본
'''
'''
두번째풀이 -  isdigit()을 새롭게 알게되었음 bool값을 리턴해줌
'''
def solution(s):
    return s.isdigit() and len(s) in [4,6]

'''
첫번째풀이
'''
def solution(s): 
    for char in s:
        if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            pass

        else:
            return False
    N = len(s)
    if N == 4 or N == 6:
        return True

    else:
        return False