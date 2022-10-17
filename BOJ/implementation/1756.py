'''
피자굽기
'''
'''
네번째풀이 - 이진탐색 풀이 정렬이였음
'''
def solution():
    ovenDepth, doughCnt = map(int, input().split())
    oven = list(map(int, input().split()))
    dough = list(map(int, input().split()))

    # 이분탐색을 위해 오름차순 정렬
    for idx in range(0, ovenDepth-1):
        if oven[idx] < oven[idx+1]:
            oven[idx+1] = oven[idx]


    def check(start, end, targetSize, limit):
        if start > end:
            return -1
        
        middle = (start + end) // 2

        if oven[middle] >= targetSize:

            if middle + 1 < limit:

                if oven[middle+1] >= targetSize:
                    #return을 해주어야됨
                    return check(middle+1, end, targetSize, limit)
            
                else:
                    return middle
            
            else:
                return middle
        
        else:
            return check(start, middle-1, targetSize, limit)

    
    res = ovenDepth #숫자 참조는 그냥 숫자 참조일뿐 객체복사가 아님주의
    for i in range(doughCnt):
        #아.. res로 바꿔줘야됨 단순 ovenDepth가 아님
        res = check(0, res, dough[i], res)

        if res == -1:
            break
    
        if res == 0 and i < doughCnt:
            break
    
    if res == -1 or res == 0:
        print(0)
    else:
        print(res+1) # 1-indexed 맞춰주면 됨 초기부터 데이터는 0-indexed로 접근한다

solution()


            




    




'''
세번째풀이 - 시간초과 최악의 경우 O(N*2)은 약 900만회 계산이 된다.. 더될 수도 있음..
최상단에서부터 피자가 최하단 D까지 지름을 거쳐가며 들여보내줘야된다.
이미 들여보내줬으면 못들어가도록 표시를 해놓아야 한다. Depthlimit가 되겠군
'''
# def solution():
#     ovenDepth, doughCnt = map(int, input().split())
#     # 현재 도우에 들어갈 수 있는지 여부 정보담긴 배열 isAvailable
#     isAvailable = [True for _ in range(ovenDepth)]
#     oven = list(map(int, input().split()))
#     dough = list(map(int, input().split()))
#     # 도우별로 값이 True인 oven까지 계속 들어간다.

#     # 완성된 반죽을 오븐에 집어넣는다.
#     # 반죽을 그만 집어넣어야되는 기준은 
#     # 그다음 오븐 뎁스가 오븐깊이를 초과하거나
#     # 그다음 오븐뎁스에 이미 다른 반죽이 존재하거나
#     # 현재도우보다 다음오븐길이보다 작은 경우에 그만 집어넣어야 한다.
#     # 단, 현재 반죽을 해당 도우에 집어넣을지 말지는 현재 도우가 현재 깊이의 오븐보다 지름이 작거나 같은 경우이고, 아무도우도 없을때에만 집어넣을 수 있다.
#     # 조건에 맞지 않는 도우는 버려야 한다.
#     finalDepthPos = ovenDepth
#     while dough:
#         nowDoughLength = dough.pop(0)
#         currentDepth = finalDepthPos

#         for depth in range(finalDepthPos):
#             if nowDoughLength <= oven[depth]:
#                 continue
#             if nowDoughLength > oven[depth]:
#                 finalDepthPos = depth - 1
        
#         print(nowDoughLength, currentDepth, finalDepthPos)
#         if currentDepth == finalDepthPos:
#             finalDepthPos -= 1

#         if finalDepthPos <= 0:
#             break

#     if len(dough) > 0: # 피자가 다 안들어 갔을때
#         print(0)
#     else:
#         print(finalDepthPos+1) # 1-indexed이므로 +1 설정해줘서 인덱스를 맞춰준다

# solution()
    

            










'''
두번째풀이 - 문제를 잘못이해했다.
상단이라고 하길래 5,6,4 단순히 각각의 지름의 길이만 보고 비교했지 그 이전에 해당 깊이까지 들어갈때 통과되는 지름의 길이제한을 고려하지 못했다.
힌트를 보고 다시 깨달았다. 
네가 잘못 이해한대로 구현은 잘되엇으나 잘못된 접근이었음
'''
# 반죽이 완성되면 그순간 현재 오븐에 현재반죽에 값을 추가해준다
# 그리고 현재 오븐지름과 현재 반죽이 값이 같으면 현재반죽을 채운다음 다시 현재반죽만큼 넣어주고 오븐은 다름껄로 넘어간다
# 만약 현재 오븐지름과 현재 반죽이 작으면? 현재반죽을 채워주고 다음 반죽으로 넘어간다 언제까지 현재반죽보이 오븐지름보다 값이 같거나 커질때까지
## 만약 현재 오븐지름과 현재반죽이 값이 같으면 반죽을 다 넣어주고 오븐은 옮긴다
## 만약 현재 오븐지름보다 현재 반죽이 많으면? 현재 반죽에서 현재 오븐지름까지만 반죽에서 빼주고, 오븐을 다음껄로 넘긴다
# 현재 오븐지름이 현재 반죽보다 값이 작으면? 다음 오븐으로 넘어간다

# def solution():
#     # 현재 반죽값 nowDoughCnt
#     nowDoughCnt = 0
#     ovenDepth, doughCnt = map(int, input().split())
#     diameterOven = list(map(int, input().split()))
#     dough = list(map(int, input().split()))

#     doughIdx = 0
#     for ovenIdx in range(ovenDepth):
#         if doughIdx >= doughCnt-1:
#             print(ovenIdx+1)
#             return
        
#         if doughIdx == doughCnt-1 and nowDoughCnt != diameterOven[ovenIdx]:
#             print(0)
#             return
        
#         if nowDoughCnt + dough[doughIdx] == diameterOven[ovenIdx]:
#             doughIdx += 1
#             continue
            
#         elif nowDoughCnt + dough[doughIdx] < diameterOven[ovenIdx]:
            
#             while nowDoughCnt < diameterOven[ovenIdx]:
#                 if doughIdx + 1 < doughCnt:
#                     nowDoughCnt += dough[doughIdx]
#                     doughIdx += 1
#                 else:
#                     print(0)
#                     return

#             if nowDoughCnt == diameterOven[ovenIdx]:
#                 # 여기서 이미 새로운 도우길이가 while문에서 추가되었기 때문에 제거해줘야됨
#                 nowDoughCnt -= diameterOven[ovenIdx]
#                 doughIdx += 1

#             elif nowDoughCnt > diameterOven[ovenIdx]:
#                 nowDoughCnt = (nowDoughCnt - diameterOven[ovenIdx])
#                 doughIdx += 1
#         else:
#             nowDoughCnt = (nowDoughCnt + dough[doughIdx]) - diameterOven[ovenIdx]
#             doughIdx += 1
        
# solution()




'''
첫번째풀이- 반죽을 오븐지름 남겨서 하면 안되었음..
'''
# def solution():
#     ovenDepth, doughCnt = map(int, input().split())
#     oven = list(map(int, input().split()))
#     doughs = list(map(int, input().split()))

#     nowDepth = 0
#     for dough in doughs:
#         for depth in range(nowDepth, ovenDepth):
#             if oven[depth] >= dough:
#                 nowDepth = depth
    
#     print(nowDepth)
# solution()



