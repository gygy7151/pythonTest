'''
LCS_2
'''
'''
네번째풀이 - 이분탐색과 메모이제이션 이용
'''            
N = int(input())
cases = list(map(int, input().split()))
vector = [0]

def lower_bound(left, right, case):
    global v_left
    global v_right
    while v_left < v_right:
        mid = (v_left + v_right) // 2
        if vector[mid] < case:
            v_left = mid + 1
        else:
            v_right = mid
    vector[v_right] = case

for case in cases:
    # 백터의 끝값이 수열의 값보다 작으면 벡터에 전부 삽입
    if vector[-1] < case:
        vector.append(case)

    else:
        # 벡터의 끝값이 수열의 값보다 큰 경우 벡터내에서 
        v_left = 0
        v_right = len(vector)
        lower_bound(v_left,v_right,case)

print(len(vector)-1)


'''
세번째풀이 - 이분탐색, lower_bound 이용 -> 시간초과..
'''
# def lower_bound(arr_start, arr_end, arr_num):
#     # temp인덱스는 vector의 맨처음부터 맨뒤에서 두번째까지 포함
#     temp = vector[arr_start:arr_end]
#     temp_idx = arr_end-1
#     while temp:
#         temp_num = temp.pop()
#         if temp_num == arr_num:
#             return
#         elif temp_num > arr_num:
#             temp_idx -= 1
#             continue
#         else:
#             vector.insert(temp_idx+1, arr_num)
#             return
            
# N = int(input())
# arr = list(map(int, input().split()))
# vector = []
# vector.append(arr[0])
# for i in range(1,N):
#     # 백터의 끝값이 수열의 값보다 작으면 벡터에 전부 삽입
#     if vector[-1] < arr[i]:
#         vector.append(arr[i])
#     # 벡터의 끝값이 수열의 값보다 큰 경우 벡터내에서 
#     elif vector[-1] > arr[i]:
#         lower_bound(0,len(vector)-1,arr[i])
# print(len(vector))

'''
두번째 풀이 - 백트래킹 - Recursion Error 대안책으로 bfs활용했으나 해결 안됨
'''
# def LIS(k):
#     global lis
#     global answer
#     q = [k]
#     while q:
#         if k >= N:
#             if lis > answer:
#                 answer = lis
#             return
#     # 선택해야되는 경우
#         if A[k] > A[k-1]:
#             lis += 1
#             LIS(k+1)
#         else:
#             LIS(k+1)
# N = int(input())
# A = list(map(int, input().split()))
# answer = 0
# for k in range(1,N):
#     lis = 0
#     LIS(k)
# print(answer)
'''
첫번째풀이 - dp 시간초과
'''
# N = int(input())
# arr = list(map(int, input().split()))
# DP = [-1] * N
# DP[0] = 1
# for i in range(1,N):
#     max_length = 0
#     for j in range(i):
#         if arr[i] > arr[j] and DP[j] > max_length:
#             max_length = DP[j]
#     DP[i] = max_length + 1

# answer = DP[0]
# for i in range(1, N):
#     answer = max(answer, DP[i])
# print(answer)




