'''
없는 숫자더하기
'''
'''
두번째풀이 - 더간단하게
'''
def solution(numbers):
    return 45 - sum(numbers)

'''
첫번째풀이 - 모든원소는 서로다른데 굳이 set으로 중복없애려시도했다. 비효율적임
'''
# def solution(numbers):
#     answer = -1
#     N = set(numbers)
#     NS = sum(N)
#     OS = (9*10) //2
#     answer = OS - NS
#     return answer
