'''
연산자 끼워넣기
'''
'''
세번째풀이- 아... 훨씬 더 쉬운 방법이 있었음
그리고 나머지 연산은 그냥 int(a / b)로 해주면 되었음...
DP도 필요 없었음..
'''
def solution():
    N = int(input())
    A = list(map(int, input().split()))
    oper = list(map(int, input().split()))

    max_val, min_val = -int(1e9), int(1e9)

    def dfs(depth, res, plus, minus, multiply, divide):
        nonlocal max_val
        nonlocal min_val
        if depth == N:
            max_val = max(res, max_val)
            min_val = min(res, min_val)
            return

        if plus:
            dfs(depth+1, res + A[depth], plus-1, minus, multiply, divide)

        if minus:
            dfs(depth+1, res - A[depth], plus, minus-1, multiply, divide)

        if multiply:
            dfs(depth+1, res * A[depth], plus, minus, multiply-1, divide)

        if divide:
            # //아니고 /임 주의
            dfs(depth+1, int(res / A[depth]), plus, minus, multiply, divide-1)

    dfs(1, A[0], oper[0], oper[1], oper[2], oper[3])

    print(max_val)
    print(min_val)
solution()

'''
두번째풀이 - dfs -틀림
'''
# # DP테이블 = DP[i] = (max(DP[i-1][0](+-*//) A[i]), min(DP[i-1][1](+-*//) A[i])
# def solution():
#     N = int(input())
#     A = list(map(int, input().split())) #0-indexed로 시작
#     # +, -, *, //
#     oper = [list(map(int, input().split()))] # 0번째 최대, 1번째 최소
#     oper.append(oper[0])
#     DP = [[0,0] for _ in range(N)]
#     DP[0][0], DP[0][1] = A[0], A[0] # 0번째열 최대, 1번째열 최소
    
#     # A의 1번째부터 N-1번째 항까지 계산해준다.
#     for idx in range(1, N):
#         max_dp, min_dp = DP[idx-1][0], DP[idx-1][1]
#         # 애초에 A[i]와 DP[i-1]값과 4칙연산한 값과 연산자를 튜플로 리스트에 넣어놓고
#         temp_max = [(max_dp+A[idx], 0),(max_dp-A[idx], 1), (max_dp*A[idx], 2)]
#         temp_min = [(min_dp+A[idx], 0),(min_dp-A[idx], 1), (min_dp*A[idx], 2)]

#         # 나눗셈은 c++14기준으로 예외처리해준다. 까다롭네..까다로워
#         if max_dp < 0 and A[idx] > 0:
#             temp_max.append((-(abs(max_dp)// A[idx]), 3))

#         elif max_dp > 0 and A[idx] < 0:
#             temp_max.append((-(max_dp// abs(A[idx])), 3))
        
#         else:
#             temp_max.append((max_dp// A[idx], 3))

#         if min_dp < 0 and A[idx] > 0:
#             temp_min.append((-(abs(min_dp)// A[idx]), 3))
        
#         elif min_dp > 0 and A[idx] < 0:
#             temp_min.append((-(min_dp// abs(A[idx])), 3))
        
#         else:
#             temp_min.append((min_dp// A[idx], 3))

#         # 정렬해서 for문 돌면서 제일 큰값과 제일 작은 값을 구해주고..
#         temp_max.sort(reverse=True)
#         temp_min.sort()

#         print(temp_max)
#         print(temp_min)
#         print(oper)
#         print('*'*50)
#         ## 연산이 있으면 DP[idx][0]과 DP[idx][1]의 값을 갱신해준다. 이땐 할당해줘야됨
#         ## oper 값도 갱신해줘야됨. 이건 max랑 min 따로 따로 해줘야됨
#         for max_num, cal in temp_max:
#             if oper[0][cal] > 0:
#                 DP[idx][0] += max_num
#                 oper[0][cal] -= 1
#                 break
        
#         for min_num, cal in temp_min:
#             if oper[1][cal] > 0:
#                 DP[idx][1] += min_num
#                 oper[1][cal] -= 1
#                 break
    
#     # 최대, 최솟값을 출력해준다.
#     print(DP[N-1][0])
#     print(DP[N-1][1])
#     print(DP)

# solution()
    



'''
첫번째풀이- 시간초과
'''
# # 만약 나눗셈할때 분자가 음수이면 양수로 바꾼뒤 몫을 취하고 다시 몫을 음수로 취한다
# from itertools import permutations
# def solution():
#     N = int(input())
#     A = list(map(int, input().split()))
#     # +, -, *, //
#     oper = list(map(int, input().split()))
#     total_oper = []

#     def add_oper(cnt, oper):
#         nonlocal total_oper
#         total_oper += [ oper for _ in range(cnt)]

    
#     for i in range(4):
#         if i == 0:
#             add_oper(oper[i], '+')
        
#         elif i == 1:
#             add_oper(oper[i], '-')

#         elif i == 2:
#             add_oper(oper[i], '*')

#         else:
#             add_oper(oper[i], '//')

#     max_val, min_val = -int(1e9), int(1e9)
    
#     for oper_set in list(permutations(total_oper, N-1)):
#         cal_res = A[0]

#         for i in range(N-1):
#             if oper_set[i] == '+':
#                 cal_res += A[i+1]
            
#             elif oper_set[i] == '-':
#                 cal_res -= A[i+1]

#             elif oper_set[i] == '*':
#                 cal_res *= A[i+1]

#             else:
#                 if A[i+1] < 0:
#                     cal_res = -(cal_res // -(A[i+1]))

#                 elif cal_res < 0:
#                     cal_res = -(-(cal_res) // A[i+1])
                
#                 else:
#                     cal_res = cal_res // A[i+1]
        
#         if max_val < cal_res:
#             max_val = cal_res
        
#         if min_val > cal_res:
#             min_val = cal_res
    
#     print(max_val)
#     print(min_val)                  

# solution()