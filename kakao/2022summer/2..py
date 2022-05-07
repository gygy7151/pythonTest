'''
테스트케이스2개 맞음. 예외를 모르겠음
'''
def solution(queue1, queue2):
    answer = 0
    target = (sum(queue1) + sum(queue2)) // 2
    n = len(queue1)
    for _ in range(n//2):
        a = queue1.pop(0)
        queue2.append(a)
        answer += 1
        sum1, sum2 = sum(queue1), sum(queue2)
        if sum(queue1) == target and sum(queue2) == target:
            return answer
        else:
            b = queue2.pop(0)
            queue1.append(b)
            answer += 1
            sum1, sum2 = sum(queue1), sum(queue2)
            if sum(queue1) == target and sum(queue2) == target:
                return answer
    sum1, sum2 = sum(queue1), sum(queue2)
    if sum(queue1) != target or sum(queue2) != target:
        answer = -1
    return answer