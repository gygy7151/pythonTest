'''
파일합치기
'''
'''
참고 코드
'''
# def calculate():
#     file_counts, file_sizes = int(input()), [0] + list(map(int, input().split()))
#     stack_sum = [0 for _ in range(file_counts+1)]
#     for i in range(1, file_counts+1):
#         stack_sum[i] = stack_sum[i-1] + file_sizes[i]
#     min_sum = [[0 for _ in range(file_counts+1)] for _ in range(file_counts+1)]
#     for some in range(2, file_counts+1): # 부분 파일의 길이
#         for first in range(1, file_counts+2-some):   # 시작점
#             min_sum[first][first+some-1] = min([min_sum[first][first+k] + min_sum[first+k+1][first+some-1] for k in range(some-1)]) + (stack_sum[first+some-1] - stack_sum[first-1])
 
#     print(min_sum[1][file_counts])
 
# for _ in range(int(input())):
#     calculate()

'''
두번째풀이 - dfs말고 2차원 dp로 풀음
'''
def calculate():
    file_size, file_s = int(input()), [0] + list(map(int, input().split()))
    stacked_sum = [0 for _ in range(file_size+1)]
    for i in range(1, file_size+1):
        stacked_sum[i] = stacked_sum[i-1] + file_s[i]
    min_cost_sum = [[0 for _ in range(file_size+1)] for _ in range(file_size+1)]
    for some in range(2, file_size+1):
        for first in range(1, file_size+2-some):
            min_cost_sum[first][first+some-1] = min([min_cost_sum[first][first+k] + min_cost_sum[first+k+1][first+some-1] for k in range(some-1)])+ (stacked_sum[some+first-1] - stacked_sum[first-1])
            
    print(min_cost_sum[1][file_size])


for _ in range(int(input())):
    calculate()
'''
첫번째 풀이 - 틀림
'''
# def dfs(before_size, file_size, temp_file_size, visited):
#     if len(temp_file_size) == K-1:
#         total = sum(temp_file_size)
#         for i in range(K):
#             if not visited[i]:
#                 total += total + file_size[i]
#         return int(total)   
#     for new_idx, next_size in enumerate(file_size):
#         if not visited[new_idx]:
#             visited[new_idx] = True
#             temp_file_size.append(file_size[new_idx] + before_size)
#             dfs(next_size, file_size, temp_file_size, visited)
#     total = sum(temp_file_size)
#     return int(1e9)

# T = int(input())
# for _ in range(T):
#     K = int(input())
#     file_size = list(map(int, input().split()))
#     temp_file_size = []
#     visited = [False] * (K)
#     for idx in range(K):
#         visited[idx] = True
#         min_total = int(1e9) + 1
#         cost = min(dfs(file_size[idx], file_size, temp_file_size, visited), min_total)
#         #모든장을 합치는데 필요한 최소비용
        # print(cost)
