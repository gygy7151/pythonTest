'''
수박수박수박수박수?
'''
'''
첫번째풀이
'''
def solution(n): 
    return "".join(['수' if i % 2 == 0 else '박' for i in range(n)])