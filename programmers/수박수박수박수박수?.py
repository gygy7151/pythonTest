'''
수박수박수박수박수?
'''
'''
두번째풀이 - 아예문자열을 미리 선언하는것도 방법
'''
def solution(n):
    return "".join(["수박"[i%2] for i in range(n)])

'''
첫번째풀이
'''
def solution(n): 
    return "".join(['수' if i % 2 == 0 else '박' for i in range(n)])