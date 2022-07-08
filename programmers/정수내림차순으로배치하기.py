'''
내림차순으로배치하기
'''
'''
두번째풀이 - 다른풀이보니깐 그냥 sort해도 상관없나봄
'''
def solution(n):
    N = list(str(n))
    N.sort(reverse=True)
    return int(''.join(N))
'''
첫번째풀이 - 시간초과날까 싶어서 Counter사용했음
'''
# from collections import Counter

# def solution(n):
#     answer = ''
#     N = Counter(list(map(int, list(str(n)))))
#     MAX = N.most_common()
#     MAX.sort(key=lambda x: -x[0])
    
#     for x,y in MAX:
#         answer += str(x) * y
#     return int(answer)