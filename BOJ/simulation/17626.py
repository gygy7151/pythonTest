'''
Four Squares
'''
'''
세번째풀이 - 수학적으로 접근 최대 4개 이하의 제곱수를 가지는점을 활용
경우의수를 4가지로 제한하고 수학적접근풀이
N의 제곱근의 올림값을 N에서 빼준값이 다시 제곱근이 되는 경우, 즉 정수가 되는경우를 각각 구함
너무 아름다운 코드임
참조 : https://simsim231.tistory.com/160
'''
def solution():
    N = int(input())

    # n제곱근이 정수일때 답은 1
    if int(N**0.5) == N**0.5:
        return 1
    
    # 1~ (N의 제곱근의 올림값을) i라고할때 N-i^2의 제곱근이 정수라면 답은 2
    for i in range(1, int(N**0.5) + 1):
        if int((N - i**2)**0.5) == (N - i**2)**0.5:
            return 2
    # (N -i^2 - i^2)의 제곱근이 정수라면 답은 3
    for i in range(1, int(N**0.5) +1):
        for j in range(1, int((N-i**2)**0.5) + 1):
            if int((N - i**2 - j**2)**0.5) == (N - i**2 - j**2)**0.5:
                return 3

    return 4
print(solution())

'''
두번째풀이 - DP로 접근 - 시간초과발생
'''
# def solution():
#     N = int(input())
#     DP = [0] * (N+1)
#     DP[1] = 1

#     for i in range(2,N+1):
#         j = 1
#         min_val = 4
        
#         while ((j**2) <= i):
#             # 이전에 최대 제곱수를 구하고 N에서 차감하던 방식에서 좀 변형된 접근
#             # 1부터 제곱수를 차례로 구하면서 N에서 차감한 수를 인덱스로 설정 (최대제곱수범위까지 인덱스값갱신하므로 자동으로 최대 제곱수구해짐)
#             # 그 인덱스 값은 차감한 수의 제곱갯수가 가장 작은걸로 갱신 이때 비교는 최대 4개까지이므로 4랑비교
#             i_th_square = DP[i-(j**2)]
#             min_val = min(min_val, i_th_square)
#             j += 1
        
#         # i랑 작거나 같을땐 상관없음 그냥 여기서 +1해주면됨 왜? 1의제곱수는 제외했기 때문에?
#         DP[i] = min_val + 1
#     return DP[N]
# print(solution())

            


'''
첫번째풀이 - 틀림
'''
# def solution():
#     N = int(input())
#     NN = N
#     ANS = 0
#     MIN = []
#     CNT = 0
#     while True:
#         for i in range(N):
#             if i**2 > NN:
#                 NN -= (i-1)**2
#                 ANS += 1
#                 break
#             elif i**2 == NN:
#                 NN -= i**2
#                 ANS += 1
#                 break

#         if ANS > 4 and NN <= 0:
#             N-= 1
#             NN = N
#             ANS = 0
#             CNT = 0

#         if ANS <= 4 and NN <= 0 :
#             MIN.append(ANS)
#         if len(MIN) >= 2:
#             break
#     return min(MIN)

# print(solution())
