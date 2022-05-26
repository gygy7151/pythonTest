'''
평범한 배낭 - 0/1 백트래킹 솔루션
'''
'''
네번째풀이 - 다시 0/1 dp로 접근
'''
N, K = map(int, input().split())
Weight = [0]
Profit = [0]

for i in range(N):
    w, p = map(int, input().split())
    Weight.append(w)
    Profit.append(p)

# kanpsack[i][j] ?
# 0번부터 i번째 아이템중에 가방이 j무게일때 선택한 가중치 최대값
knapsack = [[0] * (K+1) for _ in range(N+1)]
# 가중치를 채워보자
for item_num in range(1,N+1):
    for bag_wght in range(1,K+1):
        if bag_wght >= Weight[item_num]:
            knapsack[item_num][bag_wght] = max(knapsack[item_num-1][bag_wght], (knapsack[item_num-1][bag_wght - Weight[item_num]] + Profit[item_num]))
        else:
            knapsack[item_num][bag_wght] = knapsack[item_num-1][bag_wght]

print(knapsack[N][K])
'''
세번째풀이 - 틀림, 나누어지지 않는 물건을 Fractional sol로 나누려 시도해서 답이 틀림
'''
# N, K = map(int, input().split())
# # 아이템 길이
# S = []
# # 아이템 가중치
# P = []
# # 아이템 가성비(무게1당 가중치)
# _P = []

# # MP : Minimum Current Profits
# MP = 0
# # _MP :  Maximum Current Profits aft 'node V' or 'i 번째 item'
# _MP  = 0
# # X : whether presence of Items or not, idx = item_idx
# X = [0] * N

# for i in range(N):
#     bag_weight, bag_value = map(int, input().split())
#     S.append(bag_weight)
#     P.append(bag_value)
#     _val = P[i]//S[i]
#     _P.append((_val, S[i], i))

# def frac_knapsack(left_idx, left_size):
#     global _MP
#     _MP = 0
#     # 나머지 아이템의 가중치별로 -P에 담는다
#     left_item_value = _P[left_idx:]
#     # 가성비높은것부터 >> 길이짧은것부터 >> 사전순 정렬
#     left_item_value.sort(key = lambda x : (-x[0], x[1], x[2]))

#     # 가중치별로 하나씩 접근하면서 
#     for _p, item_size ,item_num in left_item_value:
       
#         ## 만약 left_size보다 S[노드번호]가 크면? left_size = 0 으로 만들고, (left_szie * 가중치)를 MP에 더해준다.
#         if item_size > left_size:
#             _MP += (left_size * _p)
#             return 
       
#         ## 만약 같으면? left_size에서 빼준후 MP에 P[노드번호] 더해준다.
#         elif item_size == left_size:
#             left_size -= item_size
#             _MP += P[item_num]
#             return
    
#         ## 만약 left_size보다 S[노드번호]가 작으면 left_size에서 S[노드번호]빼주고 MP에 P[노드번호] 더해준다.
#         else:
#             left_size -= item_size
#             _MP += P[item_num]

# def knapsack(i, size):
#     global MP
#     if i >= N or size <= 0:
#         return
#     # i-1번째노드까지의 가치 총합(=p) 및 사이즈총합(=s)
    
#     # P(v) = p_sum, S(v) = s_sum 계산
#     p_sum, s_sum = 0, 0
#     for v in range(i):
#         if X[v] == 1:
#             p_sum += P[v]
#             s_sum += S[v]
    
#     # X[i] = 1 = i번째 아이템을 뽑는경우
#     # 남아있는 빈공간(size)에 i번째 가방 사이즈(S[i])를 집어넣을 수 있는지 체크
#     if S[i] <= size:
#         frac_knapsack(i+1, size -(s_sum + S[i]))
#         if MP < (p_sum + P[i] + _MP):
#             X[i] = 1
#             MP = max(MP, p_sum + P[i])
#             knapsack(i+1, size - (s_sum + S[i]))
#     else:
#         frac_knapsack(i, size)
#         MP = max(MP, _MP)
#     # X[i] = 0 = i번째 아이템을 안뽑는경우
#     frac_knapsack(i+1, size)
#     if MP < (p_sum + _MP):
#         X[i] = 0
#         knapsack(i+1, size)
    
# knapsack(0, K)
# print(MP)

'''
두번째풀이 - 틀린답나옴
'''
# N, K = map(int, input().split())
# size = []
# profit = []
# answer = 0
# max_value = -(1e9)
# for _ in range(N):
#     W, V = map(int, input().split())
#     size.append(W)
#     profit.append(V)

# def dfs(item_idx, left_size, X):
#     global max_value
#     if item_idx == N:
#         result = 0
#         for i in range(N):
#             if X[i] == 1:
#                 result += profit[i]
#         print(X)
#         print(result)
#         max_value = max(max_value, result)
#         return
#     if left_size - size[item_idx] >= 0:
#         # i번째 아이템이 가방안에 존재하지않을때
#         X[item_idx] = 0
#         dfs(item_idx+1, left_size, X)
#         # i번째 아이템이 가방안에 존재할때
#         X[item_idx] = 1
#         dfs(item_idx+1, left_size - size[item_idx], X)
    
# item_presence = [0] * N
# dfs(-1,K,item_presence)

# item_value = []
# for i in range(N):
#     n = profit[i] / size[i]
#     n = round(n, 2)
#     item_value.append(n)

# min_idx_list = []
# min_value = item_value.index(min(item_value))

'''
첫번째 풀이 - 시간초과
'''
# def dfs(node,presence):
#     global added_size
#     global present_value
#     if (K - added_size) <= 0:
#         return -1
#     if node == N:
#         result = 0
#         for i in range(N):
#             if items_presence[i] == 1:
#                 result += profit[i]
#         return result
#     if presence == 1:
#         present_value += profit[node]
#         added_size -= size[node]
#         items_presence[node] = 1
#     dfs(node+1, 0)    
#     dfs(node+1, 1)

# N, K = map(int, input().split())
# size = []
# profit = []
# p_value = []
# items_presence = [0] * N
# added_size = 0
# present_value = 0

# for _ in range(N):
#     W, V = map(int, input().split())
#     size.append(W)
#     profit.append(V)
#     n = V / W
#     n = round(n, 2)
#     p_value.append(n)

# # 0 / 1 solution (0번째 아이템이 존재한다고 가정할때)
# max_value = dfs(0,1)
# print(max_value)
