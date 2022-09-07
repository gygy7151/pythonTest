'''
만취한 상범
'''
'''
두번째풀이
'''
def solution():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        room = [0]+ [1 for _ in range(N)]

        for round in range(2, N+1):
            start = 1

            while round*start <= N:
                if room[round*start]:
                    room[round*start] = 0
                else:
                    room[round*start] = 1

                start += 1
        print(room.count(1))
            
solution()

'''
첫번째풀이
'''
# def solution():
#     K = int(input())
#     M = int(input())
#     friend = [1 for _ in range(K+1)]
    
#     cal = [ int(input()) for _ in range(M)]
#     for i in range(M):
#         num = cal[i]
#         j = 1
#         while num*j <= K:
#             friend[num*j] = 0
#             j += 1

#     print(friend)
#     for i in range(1, K+1):
#         if friend[i]:
#             print(i)

# solution()
