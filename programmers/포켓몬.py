'''
포켓몬
'''
'''
세번째풀이 - 자료구조 set을활용 -> 시간복잡도해결
'''
def solution(nums):
    N = len(nums)//2
    nums = set(nums)
    NN = len(nums)
    if NN >= N:
        return N
    else:
        return NN
A = [x for x in [1,2,3,4,5]] * 2000
print(solution(A))
'''
두번째풀이 - 조합이용해서 풀이시도 - 시간초과남..
'''
# from itertools import permutations
# def solution(nums):
#     answer = 0
#     N = len(nums) // 2
#     nums = list(permutations(nums, N))
#     return max(len(x) for x in nums)

# nums = [x for x in [3,4,5]] * 3000
# print(solution(nums))
    
'''
첫번째풀이 - N/2개를 뽑는 모든 경우의수를 구하지 못함
'''
# def solution(nums):
#     N = len(nums) // 2
#     A, B= len(set(nums[:N])) , len(set(nums[N:]))
#     print(A, B)
#     return max(A,B)

# nums = [3,3,3,2,2,4]
# print(solution(nums))