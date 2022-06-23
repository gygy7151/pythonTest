'''
소수만들기
'''
'''
첫번째 풀이 - 조합 라이브러리 및 에라토스테네스의 체 활용 풀이 -> 3중for문으로 조합대체가능함
'''
from itertools import combinations
def solution(nums):
    memo = [0,0] + [1] * (3000-1)

    # 
    for i in range(2,56):
        if memo[i] == 1:
            # ** 곱셈체크 범위는 memo길이 끝까지 포함해야된다 반!드!시!
            for j in range(i*2,3001,i):
                if memo[j] != 0:
                    memo[j] = 0
    
    nums = list(combinations(nums, 3))
    
    answer = 0
    for x in nums:
        n_nums = sum(x)
        print(n_nums)
        if memo[n_nums] == 1:
            print('소수야!')
            answer += 1
    return answer

nums = [1000,999,998]
print(solution(nums))        