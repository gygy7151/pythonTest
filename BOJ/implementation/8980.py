'''
택배
'''
'''
두번째풀이- DP살짝 활용하는게 맞았음.
나는 단순히 시작점, 도착점을 기준으로 정렬했는데
도착점을 기준으로 정렬해야했었음.
왜냐, 1->5를 먼저하면 2->3이나 3->4 같은 애들은 못할 수 있기 때문임
실재로 이런애들을 카운트 못해서 최댓값을 못구했었음
'''
def solution():
    N, C = map(int, input().split())
    M = int(input())
    DP = [C for _ in range(N+1)]
    arr = []

    for _ in range(M):
        sender, receiver, boxCnt = list(map(int, input().split()))
        arr.append((sender, receiver, boxCnt))
    
    arr.sort(key= lambda x : x[1])

    answer = 0
    for sender, receiver, boxCnt in arr:
        min_val = boxCnt

        #범위 receiver까지 포함시키면 안됨. 도착지점 전까지 최솟값 구하는 거임
        for idx in range(sender, receiver):
            min_val = min(DP[idx], min_val)
        
        for idx in range(sender, receiver):
            DP[idx] -= min_val
        
        answer += min_val
        
    print(answer)
    #sum(DP[1:])이 아님. 이건 이전의 잘못된 첫번째 접근방식임
solution()



'''
첫번째풀이 - 틀림
'''
'''
최대한 많은 박스들을 배송하려고 한다
조건1. 박스를 트럭에 실으면 이 박스는 받는 마을에서만 내림
조건2. 트럭은 지나온 마을로 되돌아가지 않음.
조건3. 박스들 중 일부만 배송할 수 있음.

입력조건: 마을의 개수, 트럭의 용량, 박스정보(보내는 마을버놓, 받는 마을번호, 박스개수)
트럭 한대로 배송할 수 있는 최대 박스 수를 구하는 프로그램을 작성하시오.
단, 받는 마을 번호는 항상 보내는 마을 번호보다 크다!
'''
# def solution():
#     N, C = map(int, input().split())
#     # 택배 보내야할 정보가 담긴 2차원 배열 post
#     post = [[]for __ in range(N+1)] # 1-indexed
#     # 받는마을을 인덱스로 가진 박스갯수 정보가담긴 2차원 배열 truck
#     truck = []
#     # 현재 적재된 택배갯수 boxCnt
#     boxCnt = 0
#     # 최대 배송완료 박스수 maxBoxCnt
#     maxBoxCnt = 0

#     M = int(input())

#     for _ in range(M):
#         senderTown, receiverTown, sendBoxCnt = map(int, input().split())
#         post[senderTown].append((receiverTown, sendBoxCnt))

#     print(post)
#     for i in range(1, N+1):
#         # 택배물 하차
#         if len(truck) > 0:
#             for truckIdx in range(len(truck)):
#                 receiver, deliveryBoxCnt = truck[truckIdx]
                
#                 if receiver == i:
#                     # 반드시 truck에 해당 인덱스 제거해줘야됨
#                     boxCnt -= deliveryBoxCnt
#                     maxBoxCnt += deliveryBoxCnt
#             print(boxCnt)
#             print('빼줌')
        
#         # 택배물 상차
#         for receiverTown, sendBoxCnt in post[i]:
#             print(receiverTown, sendBoxCnt)

#             if boxCnt + sendBoxCnt <= C:
#                 truck.append((receiverTown, sendBoxCnt))
#                 boxCnt += sendBoxCnt
#                 print('더해짐')
#             else:
#                 if C-boxCnt > 0:
#                     truck.append((receiverTown,C-boxCnt))
#                     boxCnt += (C-boxCnt)
#                     break
#         print(boxCnt)
#         print(i)
#         print(truck)
#     #최종 남은것 까지 한꺼번에 배송할 수 있도록 해야
#     maxBoxCnt += boxCnt
#     print(maxBoxCnt)
# solution()




