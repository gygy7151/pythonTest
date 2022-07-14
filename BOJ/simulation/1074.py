'''
Z
'''
'''
다섯번째풀이 - 더 간단하고 알찬 풀이
'''
def solution():
    N, R, C = map(int, input().split())
    CNT = 0

    def zip(x,y,l):
        nonlocal CNT
        if x > R or x+l <= R or y > C or y+l <= C:
            #이걸 못해줘서 내가 틀린거구낭..
            CNT += l ** 2
            return

        if l > 2:

            zip(x, y, l//2)
            zip(x, y+l//2, l//2)
            zip(x+l//2, y, l//2)
            zip(x+l//2, y+l//2, l//2)

        else:
            for i, j in [(x,y), (x,y+1), (x+1,y), (x+1,y+1)]:
                if i == R and j == C:
                    print(CNT)
                    return
                CNT += 1

    zip(0,0,2**N)

solution()

'''
네번째풀이 - 반드시 CNT를 함수인자로 넘겨줘야지만 올바른 숫자를 구할 수가 있었다.
그냥 전역변수로 설정해서 구할땐 값이 제대로 갱신되지 않는걸 볼 수 있다.
재귀돌땐 특정숫자는 전역말고 지역변수로 사용하여 인자로 넘겨줄것.
'''
# def solution():
#     N, r, c = map(int, input().split())
#     # G = [[0 for _ in range(2**N)] for _ in range(2**N)]

#     def z(x,y,l, CNT):

#         if l == 2:
#             for i, j in [(x,y), (x,y+1), (x+1,y), (x+1,y+1)]:

#                 if i == r and j == c:
#                     print(CNT)
#                     return
#                 CNT += 1

#         else:
#             # 굳이 1,2,3,4사분면 모두다 돌필요없이 r과 c범위에 해당하는 사분면이면
#             # 해당값에 가기 위한 CNT를 
#             half = l//2
#             if x <= r < y + half and y <= c < y + half:
#                     z(x, y, half, CNT) #1사분면

#             elif x <= r < y + half and y + half <= c < y + l:
#                     z(x, y+half, half, CNT +(half**2) * 1) #2사분면

#             elif x + half <= r < y + half * 2 and y <= c < y + half:
#                     z(x+half, y, half, CNT + (half**2) * 2) #3사분면

#             elif x + half <= r < y + half * 2 and y + half <= c < y + l:
#                     z(x+half, y+half, half, CNT + (half**2) * 3 ) #4사분면

#     #2**N 제곱근으로 길이 표현해줘야됨
#     z(0,0,2**N, 0)

# solution()

'''
첫번째풀이/두번째풀이 - 답은맞는데 시간초과남
'''
'''
matrix를 없애고 CNT값을 따로 matrix에 저장안해 메모리효율높임
CNT만 출력하면 되는 구조이고, rc도 이미 정해져있어서 r,c인지만 인덱스확인하면됨
'''
# def solution():
#     N, r, c = map(int, input().split())
#     # G = [[0 for _ in range(2**N)] for _ in range(2**N)]
#     CNT = -1
#     ANS = 0

#     def z(x,y,l):
#         nonlocal CNT
#         nonlocal ANS
#         if l != 2:
#             z(x, y, l//2) #1사분면
#             z(x, y+l//2, l//2) #2사분면
#             z(x+l//2, y, l//2) #3사분면
#             z(x+l//2, y+l//2, l//2) #4사분면
#             return
        
#         for i, j in [(x,y), (x,y+1), (x+1,y), (x+1,y+1)]:
#             # print(i,j)
#             CNT += 1

#             if i == r and j == c:
#                 #반드시 nonlocal로 처리해줘야 해당값이 반영된다 안그러면 ANS는 동명이의어같은 객체임
#                 ANS = CNT
#                 return 
    
#     #2**N 제곱근으로 길이 표현해줘야됨
#     z(0,0,2**N)
#     return ANS

# print(solution())
'''
참조코드 출처:https://deok2kim.tistory.com/74
'''
# def Z(row, col, size, num): # (row,col: 자른 box의 첫번째 인덱스, size: box 사이즈, num: box 시작점의 숫자)
#     if size == 2: # 사이즈가 2x2가 됐을 때
#         if row == r and col == c:
#             print(num)
#             return
#         num += 1

#         if row == r and col + 1 == c:
#             print(num)
#             return
#         num += 1

#         if row + 1 == r and col == c:
#             print(num)
#             return
#         num += 1

#         if row + 1 == r and col + 1 == c:
#             print(num)
#             return
#         num += 1

#     else:
#         half_size = size // 2
#         # 왼쪽 위
#         if row <= r < row + half_size and col <= c < col + half_size:
#             Z(row, col, half_size, num)
#         # 오른쪽 위
#         elif row <= r < row + half_size and col + half_size <= c < col + size:
#             Z(row, col + half_size, half_size, num + (half_size ** 2) * 1)
#         # 왼쪽 아래
#         elif row + half_size <= r < row + half_size * 2 and col <= c < col + half_size:
#             Z(row + half_size, col, half_size, num + (half_size ** 2) * 2)
#         # 오른쪽 아래
#         elif row + half_size <= r < row + half_size * 2 and col + half_size <= c < col + size:
#             Z(row + half_size, col + half_size, half_size, num + (half_size ** 2) * 3)


# if __name__ == "__main__":
#     N, r, c = map(int, input().split())
#     Z(0, 0, 2 ** N, 0)