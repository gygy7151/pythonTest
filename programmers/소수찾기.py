'''
소수찾기 -  에라토스체를 이용하여 2이상의 최대 n제곱까지의 배수 제외하고 소수만 1남김
'''
'''
세번째풀이 - 제곱근 이용하면 더 빠름
'''
def solution(n):
    answer = 0
    MEMO = [1] * 1000001
    MEMO[0], MEMO[1] = 0, 0

    for i in range(2, int(n**(0.5))+1):

        if MEMO[i] == 1:

            for j in range(2*i, n+1, i):
                MEMO[j] = 0

    for i in range(1, n+1):

        if MEMO[i] == 1:
            answer += 1

    return answer


'''
두번째풀이 - 효율정, 정확성 모두 통과됨
'''
def solution(n):
    answer = 0
    MEMO = [1] * 1000001
    MEMO[0],MEMO[1] = 0, 0
    
    MAX = 0

    while MAX**2 <= n:
        MAX += 1

    for i in range(2, MAX+1):

        if MEMO[i] == 1:
            MEMO[i] == 1
            for j in range(2*i, n+1, i):
                #합성수 소수표시(1로 잘못표시해서 결과이상하게 나왔었음)
                MEMO[j] = 0

    for i in range(1, n+1):
        if MEMO[i] == 1:
            answer += 1

    return answer

'''
첫번째풀이
'''
# from itertools import permutations
# import math
# limit = 9999999
# eratos = [1] * (2*limit +1)
# eratos[0] = 0
# eratos[1] = 0
    
# for i in range(2, int(math.sqrt(len(eratos)))):
#     if eratos[i]:
#         for j in range(i+i, len(eratos), i):
#             eratos[j] = 0
# def solution(numbers):
#     permutaion_set = set([int("".join(item)) for i in range(7) for item in set(permutations(list(numbers), i+ 1) )])
#     prime_list = [ eratos[num] for num in permutaion_set if num != 0 and num != 1 ]
#     return sum(prime_list)
    
# numbers = '017'
# print(solution(numbers))

# piece = []
# answer = []
# def solution(numbers):
#     for num in numbers:
#         piece.append(num)
#         if num != '0':
#             bfs(num)
#     print(answer)
#     return len(answer)

# def bfs(start):
#     q = [start]
#     visited = [start]
#     while q:
#         x = q.pop(0)
#         if int(x) % int(x) == 0 and int(x) != 1 and int(x) != 0:
#             answer.append(int(x))
        
#         for p in piece:
#             if p != x:
#                 new = str(x) + str(p)
#                 if len(new) <= len(piece):
#                     visited.append(int(new))
#                     q.append(int(new))

# numbers = ''
# print(solution(numbers))
