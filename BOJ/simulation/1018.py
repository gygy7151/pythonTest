'''
체스판 다시 칠하기

맨왼쪽 윗칸이 검은색인 경우
검흰검흰검흰검흰 -> 짝수열 검은색 먼저
흰검흰검흰검흰검 -> 홀수열 흰색 먼저

맨왼쪽 윗칸이 흰색인 경우
흰검흰검흰검흰검 -> 짝수열 흰색먼저
검흰검힌검흰검흰 -> 홀수열 검은색먼저

지민이가 다시 칠해야 하는 최소 개수를 구해야됨
'''

'''
세번째 풀이 - 조건 정규화 진행, 모든 count를 res에 담아 최솟값 리턴함(해결)
'''
def check(x,y):
    global answer
    w_first_cnt = 0
    b_first_cnt = 0
    for i in range(x, x+8):
        for j in range(y, y+8):

            # 짝수행
            if i % 2 == 0:
                # 짝수열
                if j % 2 == 0:
                    if graph[i][j] != 'W':
                        w_first_cnt += 1

                    else:
                        b_first_cnt += 1
                #홀수열        
                else:
                    if graph[i][j] != 'B':
                        w_first_cnt += 1
                    else:
                        b_first_cnt += 1

            # 홀수행
            else:
                # 짝수열
                if j % 2 == 0:
                    if graph[i][j] != 'B':
                        w_first_cnt += 1
                    else:
                        b_first_cnt += 1
                
                # 홀수열
                else:
                    if graph[i][j] != 'W':
                        w_first_cnt += 1
                    else:
                        b_first_cnt += 1
    
    answer.append(w_first_cnt)
    answer.append(b_first_cnt)
           
answer = []
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

for x in range(N):
    for y in range(M):
        if (x + 7) >= N or (y + 7) >= M:
            continue
        check(x,y)
# print(answer)
print(min(answer))

'''
첫번째풀이 - 
실수1> 논리가 이상했음...-> 논리 해결(06.16.22) 근데 일부 테케 틀림
실수2> 판을 자르는건  X - 7 < N보다 작고, Y- 7 < M보다 작은 경우만 생각해야됨 -> 걍 애초에 범위를 range(N-7), range(M-7)로 잡으면 좋음
실수3> 시작하는 칸이 W로 시작할지 B로시작할지 모두 고려해야 했는데 수동적으로 주어진 상태값으로 하나의 경우만 고려해 계산해서 틀렸다.
'''
# def check(x,y):
#     global answer
#     count = 0
#     if graph[x][y] == 'B':
#         for i in range(x, x+8):
#             for j in range(y, y+8):
#                 if 0 <= i < N and 0 <= j < M:
#                     # 홀수열인경우(06.15.22) --> ***아..짝수행인데.. 그리고 열은 따로 구분해줬어야되었다.
#                     # 짝수행(06.16.22)
#                     if i % 2 == 0:
#                         if j % 2 == 0:
#                             if graph[i][j] != 'B':
#                                 count += 1

#                         else: 
#                             if graph[i][j] != 'W':
#                                 count += 1
#                     # 홀수행(06.16.22)
#                     else:
#                         if j % 2 == 0:
#                             if graph[i][j] != 'W':
#                                 count += 1
#                         else:
#                             if graph[i][j] != 'B':
#                                 count += 1

#     else:
#         for i in range(x, x+8):
#             for j in range(y, y+8):
#                 if 0 <= i < N and 0 <= j < M:
#                     # 짝수행(06.16.22)
#                     if i % 2 == 0:
#                         if j % 2 == 0:
#                             if graph[i][j] != 'W':
#                                 count += 1
#                         else:
#                             if graph[i][j] != 'B':
#                                 count += 1
#                     # 홀수행(06.16.22)
#                     else:
#                         if j % 2 == 0:
#                             if graph[i][j] != 'B':
#                                 count += 1
#                         else:
#                             if graph[i][j] != 'W':
#                                 count += 1
#     answer.append(count)

# N, M = map(int, input().split())
# graph = []
# answer = []
# for i in range(N):
#     graph.append(list(input()))

# for x in range(N):
#     for y in range(M):
#         if (x + 7) >= N or (y + 7) >= M:
#             continue
#         check(x,y)
# print(answer)
# print(min(answer))