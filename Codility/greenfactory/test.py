def solution(A):
    # write your code in Python 3.6
    # 아 이분탐색으로 풀어야겠다
    for x in range(1,10001):
        start = 0
        end = len(A) - 1
        while start <= end:    
            mid = (start + end) // 2
            if x == A[mid]:
                return x
            elif x > A[mid]:
                start = mid + 1
            else:
                end = mid - 1
A = [x for x in range(int(input()))]
print(solution(A))