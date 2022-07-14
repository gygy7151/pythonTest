'''
색종이만들기
'''
'''
두번째풀이 - double check 넣은 부분
'''
# def quad_tree(x, y, n):
#     global matrix, blue, white #주어진 배열과 색 카운트 끌어오기
#     color = matrix[y][x] #첫 색깔과 나머지 색이 같아야함
#     double_break = False #for문 탈출용 double_break
    
#     for i in range(x, x+n):
#         if double_break:
#             break
            
#         for j in range(y, y+n):
#             if matrix[j][i] != color: #하나라도 틀릴시에 재귀문 생성
#                 quad_tree(x, y, n//2) #2사분면
#                 quad_tree(x + n//2, y, n//2) #1사분면
#                 quad_tree(x, y + n//2, n//2) #3사분면
#                 quad_tree(x + n//2, y + n//2, n//2) #4사분면
#                 double_break = True #탈출!
#                 break
    
#     if not double_break:
#         if matrix[y][x] == 1: #파란색이라면
#             blue += 1
#         else:
#             white += 1 #흰색이라면



# N = int(input())
# matrix = []
# blue = 0
# white = 0

# #matrix 받기
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))
# print(matrix)
# quad_tree(0,0,N)
# print(white)
# print(blue)
'''
첫번째풀이 - 쿼드트리. Divde and Conquer  - return으로 깔끔하게 정리
'''
def solution():
    N = int(input())
    PAPER = [list(map(int, input().split())) for _ in range(N)]
    W_CNT, B_CNT = 0, 0

    def cut_paper(x,y,l):
        nonlocal W_CNT, B_CNT, PAPER
        #첫색깔과 나머지색깔이 같아야됨
        color = PAPER[x][y]

        for i in range(x, x+l):

            for j in range(y, y+l):
                if PAPER[i][j] != color:
                    #아..수식이 잘못되었네
                    cut_paper(x, y, l//2) #1사분면
                    cut_paper(x + l//2, y, l//2) #2사분면
                    cut_paper(x, y + l//2, l//2) #3사분면
                    cut_paper(x + l//2, y + l//2, l//2) #4사분면
                    return

        if color == 0:
            W_CNT += 1
        else:
            B_CNT += 1

    cut_paper(0,0,N)
    print(W_CNT)
    print(B_CNT)

solution()