'''
ACM 호텔
'''
'''
두번째풀이
'''
def solution():
    
    ANS = []
    for _ in range(int(input())):
        answer = ''
        cnt = 0
        H, W, N = map(int, input().split())
        
        for x in range(W):
            for y in range(H):
                cnt += 1
                if cnt == N:
                    Y, X = y+1, x+1
                    if X < 10:
                        X = '0' + str(X)
                    
                    answer += str(Y)
                    answer += str(X)
                    ANS.append(answer)
    return ANS

res = solution()
print(*res, sep='\n')

        


'''
첫번째풀이 - 탑다운 향식으로 접근하려했으나 오답
'''

# def solution():
    
#     ANS = []
#     for i in range(int(input())):
#         answer = ''
#         H, W, N = map(int, input().split())
#         Y = ((H * W) - N) // W
#         X = ((H * W) - N) % W
        
#         if X < 10:
#             X  = '0' + str(X)
        
#         answer += str(Y)
#         print(answer)
#         answer += str(X)
#         print(answer)

#         ANS.append(answer)
#     return ANS
        

# res = solution()
# print(*res, sep="\n")