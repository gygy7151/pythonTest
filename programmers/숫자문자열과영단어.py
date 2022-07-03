'''
숫자문자열과 영단어
'''
'''
두번째풀이
'''
#전역변수로 선언
INDEX = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9' 
}

def solution(s):
    answer = ''

    for num, digit in INDEX.items():
        s = s.replace(num, digit)
    
    answer = int(s)
    return answer


'''
첫번째풀이 - replace가 적용이 안되서 어거지로 sub을 사용했다..
'''
# def solution(s):
#     answer =  0
 
#     s = re.sub('zero', '0', s)
#     s = re.sub('one', '1', s)
#     s = re.sub('two', '2', s)
#     s = re.sub('three', '3', s)
#     s = re.sub('four', '4', s)
#     s = re.sub('five', '5', s)
#     s = re.sub('six', '6', s)
#     s = re.sub('seven', '7', s)
#     s = re.sub('eight', '8', s)
#     s = re.sub('nine', '9', s)
        
#     answer += int(s)
#     return answer
# import re