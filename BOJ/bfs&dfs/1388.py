'''
바닥장식
'''
def solution():
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    count = 0

    #행
    for i in range(N):
        #열
        j = 0
        
        while j < M:
            if board[i][j] == '|':
                j += 1
            else:
                count += 1
                while j < M and board[i][j] == '-':
                    j += 1
    
    #열
    for j in range(M):
        #행
        i = 0
        
        while i < N:

            if board[i][j] == '-':
                i += 1

            else:
                count += 1
                
                while i < N and board[i][j] == '|':
                    i += 1
        
        
    print(count)

solution()
