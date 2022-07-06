'''
평균구하기
'''
'''
첫번째풀이 - 따로 round로 감쌀필요없음
음수든 정수든 상관없..round도 마찬가지로 상관없이 리턴함
'''
def solution(arr):
    return sum(arr)/len(arr)
