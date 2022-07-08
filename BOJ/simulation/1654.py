'''
랜선자르기
'''
'''
두번째풀이 - zero division 예외처리를 할 수 잇으나 그럼 해당 mid값이 일부 누락되어지는 불상사발생
그래서 division들어간 이분탐색의 경우 1부터 시작하는게 국룰이자 안전빵임
'''
import sys
input = sys.stdin.readline
def solution():
    K, N = map(int, input().split())
    LANS = [ int(input()) for _ in range(K)]
    start = 1
    end = max(LANS)
    ANS = []
    CUT_LANS_CNT = 0
    
    while start <= end:
        mid = (start + end) // 2
        CUT_LANS_CNT_SUM = 0

        for lan in LANS:
            # 아 .. 
            # if mid > 0: - > 이래도 일부값은 답이 안됨
            CUT_LANS_CNT_SUM += (lan // mid)
        
        if CUT_LANS_CNT_SUM >= N:
            start = mid + 1
        
        else:
            end = mid - 1

        # 코드 이해하기 쉽도록 편의상 변수선언
        MAX_LENGTH = mid
        
        if CUT_LANS_CNT_SUM >= N:
            ANS.append(MAX_LENGTH)
    return max(ANS)
print(solution())

'''
첫번째풀이
'''
# import sys
# def solution():
#     K, N = map(int, input().split())
#     LANS = [int(x.rstrip()) for x in sys.stdin.readlines()]
#     # 이거하면 zerodivision 에러남
#     start = 0
#     end = max(LANS)
#     while start <= end:
#         mid = (start + end) // 2
#         SUM = 0

#         for lan in LANS:
#             SUM += (lan // mid)
        
#         if SUM < N:
#             end = mid - 1
        
#         elif SUM > N:
#             start = mid + 1

#         else:
#             return mid
# print(solution())