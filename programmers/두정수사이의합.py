'''
두정수사이의합
'''
'''
첫번째풀이
'''
def solution(a, b): 
    return sum(range(a,b+1)) if a < b else sum(range(b,a+1))