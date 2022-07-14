'''
나누어떨어지는숫자
'''
'''
두번째풀이
'''
def solution(arr, divisor):
    return sorted([ e for e in arr if e % divisor == 0]) or [-1]

'''
첫번째풀이
'''
def solution(arr, divisor):
    answer = []
    
    for e in arr:
        if e % divisor:
            continue
            
        answer.append(e)
    
    if len(answer):
        answer.sort()
        return answer
    else:
        return [-1]