'''
설탕배달
'''
'''
일곱번째풀이 - 맞음
'''
'''
바텀업 방식으로 접근
3의 갯수가 0개일때부터 시작
5로나눈 나머지를 또 3이나 5로 나누어봤자 결과는 두개밖에 없음
3보다 작거나 크면 -1일꺼고 5로나눈 나머지는 항상 4이하이기 때문에 5로 다시 나누면 1~4값이 나오므로 0이 안되서 -1일꺼임
이걸로는 명확한 3의 갯수를 구할 수없음
'''
def solution():
    SUGAR = int(input())
    POCKET = 0
    
    # N은 0보다 크거나 같을때까지 계산해줘야됨
    # 0이되면 나누어 떨어지므로 지금까지 가방갯수랑 합산해서 리턴됨
    while SUGAR >= 0:
        if SUGAR % 5 == 0:
            return SUGAR // 5 + POCKET
        else:
            SUGAR -= 3
            POCKET += 1
    return -1

print(solution())

'''
여섯번째풀이 -틀림
'''
# def solution():
#     SUGAR = int(input())
#     POCKET = 0

#     while SUGAR > 0:
#         if SUGAR % 5 == 0:
#             return SUGAR // 5 + POCKET
#         else:
#             SUGAR -= 3
#             POCKET += 1
#     return -1

# print(solution())
    

'''
다섯번째풀이 - 다른코드 참조 - 성공
변수명도 올바르고, 로직도 깔끔하고 좋당
'''
# def solution():
#     N = int(input())

#     BAG = 0
#     while N >= 0 :
#         if N % 5 == 0 :  # 5의 배수이면
#             BAG += (N // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#             return BAG
#         N -= 3  
#         BAG += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
#     return -1
# print(solution())
'''
네번째풀이 - 틀림
'''
def solution():
    N = int(input())
    ANS = []
    if N in [3, 5]:
        return 1

    if N == 4:
        return 1

    n = N // 5
    
    # 아.. 어차피 5로 나누면 나머지가 0에서 4 사이 이므로 다시 또 나머지 나눌 필요 없었음..
    for i in range(n+1):
        if (N-5*i) % 3 == 0:
            ANS.append(i + (N-5*i)// 3 )
        elif (N-5*i) % 5 == 0:
            ANS.append(i + (N-5*i)// 3)

        elif (N-5*i) == 0:
            ANS.append(i)
    if len(ANS) == 0:
        return -1
    else:
        return min(ANS)

print(solution())


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