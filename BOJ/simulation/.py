'''
스티커붙이기
'''
'''
두번째풀이
'''
# N : 행
# M : 렬
# K : 스티커개수
# R : 스티커의 행의수
# C : 스티커의 열의수
def stick(note_row, note_col):

    # 붙이지 못하는 경우 한칸이라도 존재하면 False
    for row in range(R):
        for col in range(C):
            if sticker_paper[row][col] == 1 and note[note_row + row][note_col + col] == 1:
                return False

    for row in range(R):
        for col in range(C):
            if sticker_paper[row][col] == 1:
                note[note_row + row][note_col + col] = 1
    return True

def solution(note_turn):
    global sticker_paper, R, C
    # 3
    if note_turn:
        # 90도 회전은 반드시 reversed해주어야됨
        sticker_paper = list(map(list, zip(*reversed(sticker_paper))))
        R, C = len(sticker_paper), len(sticker_paper[0])
    # 범위체크
    for note_row in range(N):
        if N - note_row < R:
            break
        for note_col in range(M):
            if M - note_col < C:
                break
            # 만약 스티커를 붙일 수 있으면 즉시 함수 종료
            if stick(note_row, note_col):
                return True
    return False

N, M, K = map(int, input().split())
note = [[0] * M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    sticker_paper = [list(map(int, input().split())) for _ in range(R)]
    
    attached = solution(False)
    for _ in range(3):
        if attached == False:
            attached = solution(True)
ans = 0
for note_row in range(N):
    for note_col in range(M):
        if note[note_row][note_col] == 1:
            ans += 1
print(ans)
'''
첫번째풀이 - 재귀 -> 틀림
'''
# N : 행
# M : 렬
# K : 스티커개수
# R : 스티커의 행의수
# C : 스티커의 열의수
# def stick(temp_sticker):
#     global answer
#     global notebook
#     for i in range(N):
#         for j in range(M):
#             if temp_sticker[i][j] == 1:
#                 notebook[i][j] = 1
#                 answer += 1

# def solution(sticker,times):
#     global stk_paper
#     temp_notebook = []
#     # 4 0도, 90도, 180도, 270도 회전시켜 봤음에도 
#     # # 스티커를 붙이지 못했다면 해당 스티커를 붙이지 않고 버린다.
#     if times == 4:
#         return
#     # 2 다른 스티커와 겹치거나 노트북을 벗어나지 않으면서
#     # # 스티커를 붙일 수 있는 위치를 찾는다. -> 여기서 잘못 계산했네.
#     for i in range(N):
#         for j in range(M):
#             if notebook[i][j] == 0:
#                 temp_notebook = [[0]* M for _ in range(N)]
#                 temp_sticker_nums = 0
#                 for x, y in sticker:
#                     nx, ny = x+i, y+j
#                     if nx < 0 or nx >= N or ny < 0 or ny > M:
#                         break
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if notebook[nx][ny] == 1:   
#                             break
#                         if notebook[nx][ny] == 0:
#                             temp_notebook[nx][ny] = 1
#                             temp_sticker_nums += 1
#                 # 3 선택한 위치에 스티커를 붙인다.
#                 if temp_sticker_nums == sticker_nums: 
#                     stick(temp_notebook)
#                     return
#     # # 만약 스티커를 붙일 수 있는 위치가 전혀 없어서 스티커를 붙이지 못했다면, 
#     # # 스티커를 시계 방향으로 90도 회전한 뒤 2번 과정을 반복
#     stk_paper = list(map(list, zip(*stk_paper)))
#     NR = len(stk_paper)
#     NC = len(stk_paper[0])
#     sticker = []
    
#     # 스티커가 노트북 범위안의 크기일때만 재귀
#     if NR <= N and NC <= C:
#         for i in range(NR):
#             for j in range(NC):
#                 if stk_paper[i][j] == 1:
#                     sticker.append((i,j))
#         solution(sticker, times+1)
     
# N, M, K = map(int, input().split())
# notebook = [[0]* M for _ in range(N)]
# answer = 0
# sticker_nums = 0
# for i in range(K):
#     R, C = map(int, input().split())
#     stk_paper = [list(map(int, input().split())) for _ in range(R)]
#     stripped_sticker = []
#     if R <= N and C <= M:
#     # 1 스티커를 회전시키지 않고 모눈종이에서 떼어낸다.
#         for s_row in range(R):
#             for s_col in range(C):
#                 if stk_paper[s_row][s_col] == 1:
#                     stripped_sticker.append((s_row,s_col))
#                     sticker_nums += 1
#         solution(stripped_sticker,0)
# print(answer)





    