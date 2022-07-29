'''
RGB 거리2
'''
'''
첫번째풀이
'''
def solution():
    for _ in range(int(input())):
        N = int(input())
        A = []
        for _ in range(2):
            A.append(list(map(int, input().split())))
        
        A[0][1] += A[1][0]
        A[1][1] += A[0][0]

        for i in range(2,N):
            A[0][i] = max(A[1][i-1],A[1][i-2]) + A[0][i]
            A[1][i] = max(A[0][i-1],A[0][i-2]) + A[1][i]
        # print(A)
        print(max(A[0][N-1] , A[1][N-1]))
print(solution())