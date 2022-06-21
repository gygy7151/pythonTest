'''
수 찾기
'''
def check(target):
    start = 0
    end = N-1
    cnt = 1
    while cnt < N:
        mid = (start+end) // 2
        if A[mid] > target:
            end = mid - 1
        elif A[mid] < target:
            start = mid + 1
        if A[mid] == target:
            return True
        cnt += 1
    return False

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))
# print(B)
for num in B:
    if check(num):
        print(1)
    else:
        print(0)

