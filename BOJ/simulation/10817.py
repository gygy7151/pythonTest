'''
세수
'''
'''
두번째풀이
'''
def solution(arr):
    nums = list(map(int, arr.split()))
    nums.sort()
    nums.pop()
    print(nums[-1])
    
solution(input())

'''
첫번째풀이 - 논리에러
아.세개의 수의 경우 A보다 작을 수 있는 경우는
B와 C 두가지 경우를 모두 고려했어야 했다..
'''
# def solution(arr):
#     A, B, C = map(int, arr.split())
    
#     if A == B and B == C and A == C:
#         print(A)
#         return
    
#     if B > A and A > C and B > C:
#         print(A)
    
#     elif A > B and B > C and A > C:
#         print(B)
    
#     elif A > C and C > B and A > B:
#         print(C)
# solution(input())