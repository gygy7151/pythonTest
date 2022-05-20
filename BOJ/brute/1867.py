'''
돌멩이제거
'''
'''
세번째풀이 - dfs
'''
n, k = map(int, input().split())
s = [[] for _ in range(n+1)]
linked_row_and_col = [0] * (n+1)
def dfs(start):
    global visited
    if visited[start] == 1:
        return 0
    visited[start] = 1
    for i in s[start]:
        if linked_row_and_col[i] == 0 or dfs(linked_row_and_col[i]):
            linked_row_and_col[i] = start
            return 1
    return 0
for _ in range(k):
    row, col = map(int, input().split())
    s[row].append(col)
for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i)
print(len(linked_row_and_col)- linked_row_and_col.count(0))


'''
두번째풀이 - 그리디 틀림
'''
# n, k = map(int, input().split())
# ground = [[0] * n for _ in range(n)]
# answer = 0
# for _ in range(k):
#     row, col = map(int, input().split())
#     ground[row-1][col-1] = 1
# # print(ground)
# while True:
#     # 행렬 최댓값 및 인덱스 초기화
#     max_row = 0
#     max_col = 0
#     max_row_idx = 0
#     max_col_idx = 0
#     # 행의 최댓값
#     for i in range(n):
#         if sum(ground[i]) > max_row:
#             max_row = sum(ground[i])
#             max_row_idx = i
#     # 열의 최댓값
#     for i in range(n):
#         col_sum = 0
#         for j in range(n):
#             col_sum += ground[j][i]
#         if col_sum > max_col:
#             max_col_idx = i
#             max_col = col_sum

#     if max_row == 0 or max_col == 0:
#         break
#     if max_row > max_col:
#         # print('행이큰경우')
#         ground[max_row_idx] = [0] * n
#         answer += 1
#     elif max_row < max_col:
#         # print('열이큰경우')
#         for i in range(n):
#             ground[i][max_col_idx] = 0
#         answer += 1
#     else:
#         # print('행열둘다큰경우')
#         ground[max_row_idx] = [0] * n
#         for i in range(n):
#             ground[i][max_col_idx] = 0
#         answer += 2
# print(answer)
    

'''
첫번째 풀이 - 틀림
'''
# n, k = map(int, input().split())
# ground = [['_'] * n for _ in range(n)]
# stone_pos = []
# answer = int(1e9)
# # 돌멩이표시 및 위치 저장
# for _ in range(k):
#     row, col = map(int, input().split())
#     ground[row-1][col-1] = 'X'
#     stone_pos.append((row-1,col-1))
# # 돌멩이 존재 가중치 합
# row_stone_count = [0] * n
# col_stone_count = [0] * n
# for pos in stone_pos:
#     row, col = pos
#     row_stone_count[row] += 1
#     col_stone_count[col] += 1
# while stone_pos:
#     max_row = max(row_stone_count)
#     max_row_idx = row_stone_count.index(max_row)
#     max_col = max(col_stone_count)
#     max_col_idx = col_stone_count.index(max_col)
#     if max_row == 0 and max_col == 0:
#         break
#     if row_stone_count[max_row_idx] > col_stone_count[max_col_idx]:
#         row_stone_count[max_row_idx] = 0
#         answer += 1
#     elif row_stone_count[max_row_idx] < col_stone_count[max_col_idx]:
#         col_stone_count[max_col_idx] = 0
#         answer += 1
#     else:
#         row_stone_count[max_row_idx] = 0
#         col_stone_count[max_col_idx] = 0
#         answer += 2

# print(answer)
    