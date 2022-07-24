'''
리모콘
'''
'''
세번째풀이
'''
def solution():
    target = int(input())
    ans = abs(100 - target)
    M = int(input())
    #고장난게 있을경우만 인풋받음
    if M:
        broken = set(input().split())
    else:
        broken = set()
    
    #작은수에서 큰수로 이동할땐 50만까지 보면 되지만
    #큰수에서 작은수로 이동할수도 있으므로 백만까지 봐줘야됨
    for num in range(1000001):
        for digit in str(num):
            if digit in broken:
                break
        #와..for문이 안전하게 실행되면 다음구문이 실행되도록하게 해주는 else in for loop!!
        else:
            ans = min(ans, len(str(num)) + abs(num - target))
        #그냥 아래와 같이 하면 break문을 벗어나고 무조건 ans를 구해주게끔 되어 있다..
        # ans = min(ans, len(str(num)) + abs(num - target))

    return ans
print(solution())

# target = int(input())
# ans = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
# M = int(input())
# if M: # 고장난게 있을 경우만 인풋을 받음
#     broken = set(input().split())
# else:
#     broken = set()

# # 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# # 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
# for num in range(1000001): 
#     for N in str(num):
#         if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
#             break
#     else: # 번호를 눌러서 만들 수 있는 경우엔
#     	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
#         ans = min(ans, len(str(num)) + abs(num - target))

# print(ans)

'''
두번째풀이 - 틀림
'''
# def solution():
#     btnState = [1 for _ in range(10)] 
#     nowChannel = 100
#     targetChannel = int(input())
#     brokenBtnCnt = int(input())
    
#     if brokenBtnCnt == 0:
#         return len(str(targetChannel))

#     if targetChannel == nowChannel:
#         return 0
    
#     brokenBtns = list(map(int, input().split()))
#     # 0은 사용불가를 의미
#     for i in range(brokenBtnCnt):
#         btnState[brokenBtns[i]] = 0
    
#     tempString = str(targetChannel)

#     if btnState.count(1):
#         btnNumber = 0
#     else:
#         btnNumber = -1

#     if btnNumber == -1:
#         return abs(targetChannel - nowChannel)

#     answer = int(1e9)
    
#     for minBtn in range(10):
#         if btnState[minBtn] == 1:
#             counting = 0
#             tempString = ''

#             for btn in str(targetChannel):
#                 if btnState[int(btn)] == 1:
#                     counting += 1
#                     tempString += str(btn)
                
#                 else:
#                     counting += 1
#                     tempString += str(minBtn)
#             # print(tempString)
#             M = len(str(targetChannel))
#             # print(str(minBtn) * M)
#             subCounting = abs(M + int(str(minBtn) * M) - targetChannel)
#             answer = min(answer, subCounting)
#             counting += abs(int(tempString) - targetChannel)
#             answer = min(answer, counting)

#             #아니면 그냥 minBtn으로 쭉 숫자만들기

    
#     answer = min(answer, abs(targetChannel - nowChannel))
#     return answer
    
# print(solution())


'''
첫번째풀이
'''
# def solution():
#     channelState = [1 for _ in range(10)] 
#     targetChannel = int(input())
#     brokenBtnCnt = int(input())
    
#     if brokenBtnCnt != 0:
#         brokenBtns = list(map(int, input().split()))
#         # 0은 사용불가를 의미
#         for i in range(brokenBtnCnt):
#             channelState[brokenBtns[i]] = 0
    
#     print(channelState)
#     # print(channelState)
#     nowChannel = 100
#     answer = int(1e9)

#     if targetChannel == nowChannel:
#         return 0

#     #단순히 +나 -버튼으로 조작했을때 누른횟수
#     answer = min(answer , abs(targetChannel-nowChannel))

#     #0부터 시작하여 맨처음 등장하는 최소버튼넘버를 최솟값으로 설정
#     ##이게 아니라 모든 버튼값 돌아봐야되네..
#     if brokenBtnCnt != 0:
#         minBtn = -1
#         for i in range(10):
#             if channelState[i] == 1:
#                 minBtn = 0
#     else:
#         minBtn = 0
        
#     noMoreBtn = False
#     if minBtn == -1:
#         noMoreBtn = True

#     mostRelatedBtn = 0
#     if not noMoreBtn:
#         for i in range(10):
#             if channelState[i] == 1:
#                 mostRelatedBtn = i
    
#             tempString = ''
#             tempTarget = str(targetChannel)
#             #어차피 target길이만큼 버튼은 눌러야할까?아니야..
#             #아예없는경우도 발생할 수 있어..
#             counting = 0

#             for channel in tempTarget:
#                 if channelState[int(channel)] == 1:
#                     counting += 1
#                     tempString += str(channel)
                
#                 elif channelState[int(channel)] != 1:
#                     counting += 1
#                     tempString += str(mostRelatedBtn)

#             print(tempString)
#             #그리고 나서 한번 확인해줘 target값이랑 같은지 다른지
#             #만약에 같으면 answer랑 counting 값 비교해서 최소값 리턴해주면 되고
#             #만약 다르면 target값과 int(tempString)의 절대값만큼 counting에 더해주고 answer랑 counting 값 비교해서 최소값 리턴해주면 되고
#             if int(tempString) != targetChannel:
#                 counting += abs(targetChannel - int(tempString))
#             answer = min(answer, counting)
    
#     return answer
# print(solution())