'''
정수제곱근판별
'''
'''
세번째풀이 - n이 제곱근으로 나누어떨어지면 +1하고 제곱한값 리턴하고 아니면 -1 리턴하기
메소드 안이용함
'''
def solution(n):
    return (n**(0.5)+1)**2 if not n % n**(0.5) else -1

'''
두번째풀이 -  n**(0.5)를 활용
'''
# def solution(n):
#     sqrt = n**(0.5)
#     if n % sqrt == 0:
#         return (sqrt+1)**2
#     else:
#         return -1

'''
첫번째풀이 - 그냥 해당 인덱스 끊어서 삭제하고 대입하기
'''
# def solution(n):
#     answer = 0
#     i = 1
#     if n == 1:
#         return 4

#     while i**2 < n:
#         i += 1
    
#     if i**2 == n:
#         answer = (i + 1)**2
#     else:
#         answer = -1

#     return answer