'''
실패율
'''
'''
세번째풀이
'''
def solution(N, stages):

    STAGE_MEMO = [0 for _ in range(N+2)]
    FAIL = []
    for stage in stages:

        STAGE_MEMO[stage] += 1

    #print(STAGE_MEMO)

    for i in range(N):
        tried_player = sum(STAGE_MEMO[i+1:])
        failed_player = STAGE_MEMO[i+1] 
        
        if tried_player == 0:
            FAIL.append((0,i+1))

        else:
            FAIL.append((( failed_player / tried_player), i+1))

    FAIL = sorted(FAIL, key= lambda x : ( -x[0], x[1]))
    answer = [ y for x, y in FAIL]
    

    return answer

'''
두번째풀이 - 실패
'''
def solution(N, stages):

    answer = []
    MEMO = [0] * (len(stages) + 1)
    UNCLEAR = [0] * (N+2)
    FAIL = [] 
    stages.sort() 
    stages = [0] + stages
    
    for i in range(1, N+2):

        cnt = 0
        for stage in stages:

            if MEMO[i] == 0 and stage == i:
                cnt += 1

        UNCLEAR[i] = cnt
    
    

    if sum(UNCLEAR[:N+1]) == 0 and UNCLEAR[N+1] >= 1:
        answer = [N+1] + [ x for x in range(1,N+1)]
        return answer

    clear = len(stages)-1
    # 스테이지별 실패율 분석
    for i in range(1,N+1):
        
        if clear == 0:
            FAIL.append((0,i))

        unclear = UNCLEAR[i]


        if clear == len(stages) and unclear == 0:
            if i < N:
                RATIO = 0
            else:
                RATIO = 1
        else:
            RATIO = unclear / clear

        clear -= UNCLEAR[i]
        FAIL.append((RATIO, i))
        


    FAIL = sorted(FAIL, key = lambda x : (-x[0], x[1]))

    answer = [ y for x, y in FAIL]

    return answer

'''
첫번째풀이 - 실패
'''
# def solution(N, stages):

#     answer = []
#     FAIL = [] 
#     stages.sort() 
#     RUNNER = len(stages)

#     for stage in range(1,N+2): 

#         if stage == N+1:
#             break
        
#         # 클리어못한 플레이어수 구하기
#         UNCLEAR = 0
        
#         for user in stages:

#             if int(user) == stage:

#                 UNCLEAR += 1 

#             else:
#                 break


#         if UNCLEAR >= 1:
#             stages = stages[UNCLEAR:]


#         # 클리어한 플레이어수 구하기
#         CLEAR = RUNNER - UNCLEAR
        

#         # 실패율구하기 및 데이터추가
#         if UNCLEAR != 0 and CLEAR != 0:
#             RATIO = (UNCLEAR/CLEAR) * 10000

#         else:
#             if UNCLEAR == 0:
#                 RATIO = 0

#             elif CLEAR == 0:
#                 RATIO = 1

#         FAIL.append((RATIO, stage)) 

#         # 남은 플레이어수 갱신하기
#         RUNNER = CLEAR




#     # 실패율이 높은 스테이지부터 내림차순으로 정렬한 배열 리턴
#     ## 단, 같은 실패율인경우 스테이지 번호 사전순으로 정렬
#     FAIL = sorted(FAIL, key = lambda x : (-x[0], x[1]))

    
#     # answer에 FAIL 1번째 요소만 담기
#     answer = [ y for x, y in FAIL]

#     return answer