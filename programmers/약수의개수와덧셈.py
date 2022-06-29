'''
약수의개수와 덧셈
'''
'''
두번째풀이 - 시간짧게 걸림
제곱근이 정수가 되는경우 약수가 홀수개임을 활용
'''
def solution(left,right):
    answer = 0
    for i in range(left, right+1):
        #약수는 홀수개인경우
        if int(i**0.5) == i**0.5:
            answer -= i
        #약수는 짝수개인경우
        else:
            answer += i
    return answer

'''
첫번째풀이 - 시간오래걸림
'''
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         cnt = 0
        
#         if i == 1:
#             answer -= 1
#             continue

#         for j in range(1,i+1):
#             if i % j == 0:
#                 cnt += 1
        
#         if cnt % 2 == 0:
#             answer += i
#         else:
#             answer -= i

#     return answer