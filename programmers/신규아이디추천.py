'''
신규아이디추천
'''
'''
두번째풀이
'''

# 3단계만
while '..' in answer:
    answer = answer.replace('..', '.')

'''
첫번째풀이
'''
'''
규칙에 맞지 않는 아이디 입력시
입력된 아이디와 유사하지만 규칙에 맞는 아이디 추천 프로그램개발

길이는 3자이상 15자이하
알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 문자만 사용가능
마침표는 처음과 끝에 사용할 수 없고 연속으로 사용불가능

'''
import re
def solution(new_id):
    answer = ''
    # 1
    if not new_id.islower():
        new_id = new_id.lower()
    # 2
    new_id = ''.join(re.split('[^0-9._a-z-]', new_id))

    # 3 여기서 .길이 상관없이 다 대체 되도록 하려면 어떻게 해야 했을까
    new_id = new_id.replace('......','.').replace('.....','.').replace('....','.').replace('...', '.').replace('..', '.')

    # 4
    new_id = new_id.strip('.')
    # 5
    if not len(new_id):
        new_id = 'a'

    #6
    if len(new_id) >= 16:
        new_id = new_id[0:15].strip('.')

    #7
    if len(new_id) <= 2:
        new_id = new_id + ''.join([ new_id[-1] for _ in range(3 - len(new_id))])

    return new_id