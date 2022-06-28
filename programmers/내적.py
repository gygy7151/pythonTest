'''
내적
'''
'''
두번째 풀이 - zip함수이용
'''
def solution(a, b):
    return sum(list(x*y for x, y in zip(a,b)))

'''
첫번째 풀이 - for문이용
'''
# def solution(a,b):
#     answer = 0
#     N = len(a)
    
#     for i in ragne(N):
#         ab_sum = a[i] * b[i]
#         answer += ab_sum
    
#     return answer
