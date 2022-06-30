'''
크레인인형뽑기
'''
'''
두번째 풀이 -> 미리 길이를 고려해 0을 집어넣어줘도 좋다. 인형들은 1부터시작하므로 0을 넣어주면됨
'''
def solution(board, moves):
    answer = 0
    M  = len(board[0])
    board = list(map(list, zip(*board)))
    S = [0]
    while moves:
        N = moves.pop(0) - 1
        for i in range(M):
            if board[N][i] != 0:
                if board[N][i] == S[-1]:
                    S.pop()
                    answer += 2
                else:
                    S.append(board[N][i])
                board[N][i] = 0
                break
    return answer

B = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
move = [1,5,3,5,1,2,1,4]
print(solution(B,move))

'''
첫번째 풀이 - 진짜 인형뽑기처럼 생각하고 접근했다.
그리고 애시당초 집어넣기 전에 같은지 판별하고
같으면 굳이 안넣고 맨마지막꺼만 빼줬다.
논리가 중복되는 코드들이 있어서 두번째 풀이에선 해당부분을 수정해보면 좋겟다.
'''
# def solution(board, moves):
#     answer = 0
#     M = len(board[0])
#     board = list(map(list, zip(*board)))
#     S = []
#     while moves:
#         N = moves.pop(0) - 1
#         for i in range(M):
#             if board[N][i] == 0:
#                 continue
                    
#             if len(S) >= 1:
#                 if S[-1] == board[N][i]:
#                     board[N][i] = 0  
#                     S.pop()
#                     answer += 2
#                 else:
#                     S.append(board[N][i])
#                     board[N][i] = 0  
#             else: 
#                 S.append(board[N][i])
#                 board[N][i] = 0  
#             break   
#     return answer