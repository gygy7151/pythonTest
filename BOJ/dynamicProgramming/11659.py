'''
구간합구하기4
'''
'''
네번째풀이
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0,0)
    d = [0]

    for i in range(1,N+1):
        d.append(d[i-1] + a[i])

    for _ in range(M):
        i, j = map(int, input().split())
        print(d[j] - d[i-1])

solution()
'''
세번째풀이 - 인덱스에러
'''
# def solution():
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))
#     nums.insert(0,0)
#     dp = [0 for _ in range(10)]
#     dp[1] = nums[1]

#     for i in range(2, N+1):
#         dp[i] = dp[i-1] + nums[i]
    
#     for _ in range(M):
#         x, y = map(int, input().split())
#         print(dp[y] - dp[x-1])

# solution()




'''
두번째풀이
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))

#     #변수를 활용해 이전값 차근차근더해줄것
#     sum_val = 0
#     #연결리스트로 접두사합 추가해주고
#     P = [0]
#     for num in A:
#         sum_val += num
#         P.append(sum_val)
    
#     for _ in range(M):
#         left, right = map(int, input().split())
#         print(P[right] - P[left-1])

# solution()

'''
첫번째풀이 - 시간초과
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
    
#     # 접두사합 저장
#     P = [0 for _ in range(N+1)]
#     # ***이부분에서 O(NM)으로 상당한 시간초과 발생함
#     for i in range(1,N+1):
#         P[i] = sum(A[idx] for idx in range(0,i))

#     for _ in range(M):
#         LEFT, RIGHT = map(int, input().split())
#         print(P[RIGHT] - P[LEFT-1])

# solution()

