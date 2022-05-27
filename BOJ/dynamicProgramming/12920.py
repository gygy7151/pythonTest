'''
평범한 배낭2 - 0/1 백트래킹 솔루션
'''
'''
두번째 풀이 - 이진수 활용
'''
knapsack = [0] * 10001
N, M  = map(int, input().split())
for i in range(N):
    i_wght, i_prft, i_cnts = map(int, input().split())
    exponent = 1
    smaller_expnt = 0
    while i_cnts > 0:
        smaller_expnt = min(i_cnts, exponent)
        for max_i_wght in range(M, i_wght*smaller_expnt-1, -1):
            knapsack[max_i_wght] = max(knapsack[max_i_wght - i_wght*smaller_expnt] + i_prft*smaller_expnt, knapsack[max_i_wght])
        exponent *= 2
        i_cnts -= smaller_expnt

ans = 0
for i_num in range(M+1):
    ans = max(knapsack[i_num], ans)
print(ans)
        
'''
첫번째 풀이 - 메모리 초과 , dp이용
'''
# N, K = map(int, input().split())
# P = [(0,0,0)]
# for i in range(N):
#     itm_wght, itm_prfts, itm_cnts = map(int, input().split())
#     itm_val = itm_prfts / itm_wght
#     itm_val = round(itm_val, 2)
#     for _ in range(itm_cnts):
#         P.append((itm_wght, itm_prfts, itm_val))

# P.sort(key = lambda x : (-x[2], x[1]))
# W = [0]
# V = [0]
# for data in P:
#     W.append(data[0])
#     V.append(data[1])
# itm_count = len(P)
# knapsack = [[0] * (K+1) for _ in range(itm_count+ 1)]

# for itm_num in range(1, itm_count+1):
#     for bag_size in range(1, K+1):
#         if bag_size < W[itm_num]:
#             knapsack[itm_num][bag_size] = knapsack[itm_num-1][bag_size]
#         elif bag_size > W[itm_num]:
#             knapsack[itm_num][bag_size] = max(knapsack[itm_num-1][bag_size-W[itm_num]]+V[itm_num], knapsack[itm_num-1][bag_size])
#         elif bag_size == W[itm_num]:
#             knapsack[itm_num][bag_size] = max(V[itm_num],knapsack[itm_num-1][bag_size])

# print(knapsack[itm_count][K])
