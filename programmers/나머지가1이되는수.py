'''
나머지가1이되는수
'''
'''
두번째풀이 - 더 간단하게 근데 1번풀이보다 2ms 느림
'''
def solution(n):
    return [x for x in range(2,n+1) if n % x == 1][0]

'''
첫번째풀이 
'''
# def solution(n):
#     answer = 0
#     if n % 2 == 1:
#         answer = 2
#         return answer
#     for i in range(3,n+1):
#         if n % i == 1:
#             answer = i
#             return answer