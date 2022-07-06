'''
설탕배달
'''
'''
네번째풀이 - 다른코드 참조
변수명도 올바르고, 로직도 깔끔하고 좋당
'''
def solution():
    N = int(input())

    BAG = 0
    while N >= 0 :
        if N % 5 == 0 :  # 5의 배수이면
            BAG += (N // 5)  # 5로 나눈 몫을 구해야 정수가 됨
            return BAG
        N -= 3  
        BAG += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
    return -1
print(solution())
'''
세번째풀이
'''
# def solution():
#     N = int(input())
#     ANS = int(1e9)
#     if N in [3, 5]:
#         return 1

#     if N == 4:
#         return 1

#     n = N // 5

#     for i in range(n+1):
#         if (N-5*i) % 3 == 0:
#             ANS = min(ANS, i + (N-5*i)// 3 )
#         elif (N-5*i) % 5 == 0:
#             ANS = min(ANS, i + (N-5*i)// 3 )

#         elif (N-5*i) == 0:
#             ANS = min(ANS, i)

#     if ANS == int(1e9):
#         ANS = -1
#     return ANS
# print(solution())


'''
두번째풀이,세번째풀이 - 아... N//5하면 N의 범위가 3이상이라서 for문이 안돌게된다.
예외처리를 해주거나 아니면 범위를 N//3 + 1 해준느걸로 접근해야한다.
나는 후자로 접근하겠음 -그래도 틀림
'''
# def solution():
#     N = int(input())
#     ANS = int(1e9)
#     for i in range((N//3)+1):
#         if (N - 3*i)% 5 == 0:
#             ANS = min(ANS, (N- 3*i)//5 + i)
#     return ANS
# print(solution())

'''
첫번째풀이 - 아... 조건문 if절로 각각 따로 해줬어야했다..무조건 한번씩 체크해줘야 했기 때문..주의하자
- 17반례존재.. -1이아니라 5가 답인데 -1이 나옴.
-틀림
'''
# def solution():
#     N = int(input())
#     ANS = int(1e9)

#     if N % 3 == 0:
#         ANS = min(ANS, N//3)


#     if N % 5 == 0:
#         ANS = min(ANS, N//5)


#     if (N % 5)% 3 == 0:
#         ANS = min(ANS, N//5 + (N%5)//3)


#     if (N % 3)% 5 == 0:
#         ANS = min(ANS, N//3 + (N%3)//5)

#     return ANS if ANS != int(1e9) else -1
# print(solution())