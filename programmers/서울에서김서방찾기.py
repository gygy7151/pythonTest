'''
서울에서김서방찾기
'''
'''
두번째풀이 - 맞음
'''
def solution(seoul):
    answer = seoul.index('Kim') 
    return "김서방은 {idx}에 있다".format(idx = answer)

'''
첫번째풀이 - 틀림 - 초기 sort하면 안되는거였는데 순서무시하고 내맘대로 바꿔버림
'''
def solution(seoul):
    start = 1
    end = len(seoul)
    seoul.sort()
    answer = ''

    while start <= end:
        mid = (start + end) // 2
        
        if seoul[mid] > 'Kim':
            end = mid - 1

        elif seoul[mid] < 'Kim':
            start = mid + 1

        else:
            answer = str(mid)
            # 실수** 루프탈출 깜빡했다.
            break
    # {}안에 이름을 지어줄때 인자 매칭은 ':'가 아니라 '='이다
    return "김서방은 {idx}에 있다".format(idx = answer) 