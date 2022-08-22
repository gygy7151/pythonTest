'''
트럭
'''
'''
두번째풀이
'''
def solution():
    n, w, l = map(int, input().split())
    trucks = list(map(int, input().split()))

    bridge = [0] * w
    weight, time = 0, 0

    while True:
        out = bridge.pop(0)
        weight -= out

        if trucks:
            if weight + trucks[0] <=  l:
                bridge.append(trucks[0])
                weight += trucks[0]
                trucks.pop(0)
            
            else:
                bridge.append(0)

        time += 1

        if not bridge:
            break
    print(time)
solution()




'''
첫번째풀이 - 틀림
'''
# def solution():
#     n, w, L = map(int, input().split())
#     print(w)
#     trucks = list(map(int, input().split()))
#     bridge = []
#     stackSum = 0
#     minTime = 0

#     for i in range(n):
        
#         if len(bridge) < w and stackSum + trucks[i] <= L:
#             bridge.append(trucks[i])
#             stackSum += trucks[i]

#         elif len(bridge) == w and stackSum + trucks[i] == L:
#             minTime += w
#             bridge = []
#             stackSum = 0

#         elif len(bridge) == w and stackSum + trucks[i] < L:
#             minTime += w
#             bridge = [trucks[i]]
#             stackSum = trucks[i]
                
#         elif stackSum + trucks[i] > L:
#             minTime += w
#             bridge = []
#             stackSum = 0

#         print(minTime)

#     print(minTime)

# solution()