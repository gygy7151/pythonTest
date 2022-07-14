'''
같은숫자는싫어
'''
'''
두번째풀이
'''
def solution(arr):
    answer = []
    for el in arr:
        # el을 리스트로 감싼이유는 리스트끼리 비교하기 위해서
        # answer이 빈배열일때를 고려하여 answer[-1]로 안하고 answer[-1:] 로 리스트끼리 비교함 천재임..
        # 단 answer[-1:]은 맨 마지막 요소만 담긴 리스트임
        if answer[-1:] != [el]:
            answer.append(el)
    return answer

'''
첫번째풀이
'''
def solution(arr):
    MEMO = [1] * len(arr)
    pre = arr[0]

    for idx in range(1, len(arr)):
        
        if arr[idx] == pre:
            MEMO[idx] = 0

        else:
            pre = arr[idx]

    answer =[]
    for i in range(len(arr)):
        if MEMO[i] == 1:
            answer.append(arr[i])

    return answer