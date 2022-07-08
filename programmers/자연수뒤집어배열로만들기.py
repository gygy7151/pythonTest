'''
자연수뒤집어배열로만들기
'''
'''
세번째풀이 reversed는 객체를 리턴함
'''
def solution(n):
    return list(map(int,reversed(str(n))))

'''
두번째풀이
'''
def solution(n):
    return list(map(int,str(n)))[::-1]

'''
첫번째풀이
'''
# def solution(n):
#     N = list(map(int, str(n)))
#     N.reverse() 
#     return N