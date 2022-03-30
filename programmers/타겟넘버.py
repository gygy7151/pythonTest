'''
타겟넘버 - dfs/bfs
'''
numbers = [4, 1, 2, 1]
target = 3

   

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(val, cnt):
        if cnt == n:
            if val == target:
                nonlocal answer
                answer += 1
        else:
            dfs(val+numbers[cnt], cnt+1)
            dfs(val-numbers[cnt], cnt+1)
    dfs(0,0)
    return answer

solution(numbers, target)
