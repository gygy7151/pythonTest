'''
구간합구하기 5
'''
'''
참조코드
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))

#     #변수를 활용해 이전값 차근차근더해줄것
#     sum_val = 0
#     #연결리스트로 접두사합 추가해주고
#     P = [0]
#     for num in A:
#         sum_val += num
#         P.append(sum_val)
    
#     for _ in range(M):
#         left, right = map(int, input().split())
#         print(P[right] - P[left-1])

# solution()

'''
두번째풀이 - DP
'''
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    G = []
    DP = []
    
    for i in range(N):
        sumVal = 0
        sumList = []
        data = list(map(int, input().split()))
        G.append(data)

        for a in data:
            sumVal += a
            sumList.append(sumVal)
        DP.append(sumList)
    
    print(DP)
    
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        answer = 0

        for i in range(x1-1, x2):
            answer += (DP[i][y2-1] - DP[i][y1-2])
            if x1 == 1:
                # print(answer)
                print(DP[i][y2-1])
                print(DP[i][y1-2])
        
        print(answer)

solution()

    


    


    

    



'''
첫번째풀이 - 시간초과
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N, M = map(int, input().split())
#     G = []
#     DP = []
    
#     for _ in range(N):
#         G.append(list(map(int, input().split())))
    
#     for _ in range(M):
#         x1, y1, x2, y2 = map(int, input().split())
#         res = 0

#         for i in range(x1-1, x2):
#             res += sum(G[i][y1-1:y2])

#         print(res)

# solution()
