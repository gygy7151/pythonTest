'''
개수 세기
'''
'''
첫번째풀이
'''
def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    print(nums.count(int(input())))
solution()


def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    answer = 0
    for num in nums:
        if num == N:
            answer += 1
    print(answer)
solution()
