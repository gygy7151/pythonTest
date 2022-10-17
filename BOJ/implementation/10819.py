'''
차이를 최대로
'''
'''
두번째풀이 - 순열을 활용
'''
from itertools import permutations
def solution():
    N = int(input())
    arr = list(map(int, input().split()))
    answer = -1

    for nums in list(permutations(arr, N)):
        temp = 0
        #아.. 0,1인덱스 숫자 계산하고 다시 1,2인덱스 숫자 계산하는거였는데 잘못 구현했다.
        for i in range(N-1):
            temp += abs(nums[i] - nums[i+1])

        answer = max(answer, temp)


    print(answer)
solution()






'''
첫번째풀이 - 틀림
'''
# def solution():
#     N = int(input())
#     nums = list(map(int, input().split()))
#     max_val = 0
#     nums.sort()
#     while len(nums) >= 2:
#         A = nums.pop()
#         B = nums.pop(0)
#         print(A, B)
#         max_val += abs(A-B)

#     if nums:
#         max_val += nums.pop()
    
#     print(max_val)

# solution()

