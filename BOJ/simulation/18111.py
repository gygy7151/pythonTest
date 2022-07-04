'''
마인크래프트
'''
'''
N : 세로
M : 가로
B : 인벤토리 (0 <= B <= 6.4 * 10**7) ㅁ친갯수..

1번작업: (i,j)좌표에 블록을 하나 제거 - 2초걸림
2번작업: 하나 추가하는 작업만 가능 - 1초걸림
'''
'''
세번째풀이 - 해쉬 객체 Counter 활용 
처음엔 틀렸는데
빼줘야할 부분이 인벤하고 걸려서
끝까지 item 다돌고
빼줄부분을 따로 카운팅 하는게 올바른 접근이고 정답이었다.
그냥 단순히 posiible_time = False로 체크한다고 정확하게 내가 원하는 값이 구해지는게 아니었다.
뭔가 갭차이가 존재하나봄 Inven에 값을 계속 더해줄 수 있는데 뒤 과정이 생략되어서
그런거였음!!!!!띠용......
그래서 break 안했는데도 틀렸음. 왜냐면 값이 더 더해져서 빠지는걸 충족시킬 수 있는 경우가 발생하기 때문이엇음!!!
아하.. 좀 더 동적으로 생각하질 못했었다.
앞으로 갯수 빼기할땐 함부로 False체크하지 말고 빼는 갯수 따로 더하는 갯수 따로 
비교해주는게 좋겠다. 
'''
import sys
from collections import Counter
input = sys.stdin.readline

def find_min_time(G, B):
    NG = Counter(G)
    T = []
    for H in range(max(NG.keys()), -1, -1):
        NT = 0
        # 늘 인벤갯수를 기존 갯수로 초기화 시켜주어야 된다. 
        # 단, 함수 안의 또 함수안의 변수에서 넘겨받은 인자값은 불변객체이므로 굳이 0으로 초기화 안해줘도됨
        INVENTORY = B
        # 뺄때 함께 빼주지말고
        MINUS_INVEN_CNT = 0
        # h_cnt = h높이 누적갯수
        # NG엔 Counter로 땅높이 갯수를 카운팅해서 메모해놓은 딕셔너리 객체임
        for h, h_cnt in NG.items():
            if H < h:
                INVENTORY += (h - H) * h_cnt
                NT += 2 * (h - H) * h_cnt
            
            elif H > h:
                MINUS_INVEN_CNT += (H - h) * h_cnt
                # h랑 H랑 순서 뒤바껴서 실패했음
                NT += (H - h) * h_cnt

        # 인벤보다 빼야할 갯수가 같거나 적은경우
        if INVENTORY >= MINUS_INVEN_CNT:
            T.append((NT, H))
    
    T.sort(key=lambda x : (x[0], -x[1]))
    return T[0]

def solution():
    N,M,B = map(int, input().split())
    # Counter에는 리스트 하나만 들어가야 된다. 2차원3차원은 안됨
    G = []

    for _ in range(N):
        G.extend(list(map(int, input().split())))

    ANS = find_min_time(G, B)
    return ANS

res = solution()
print(*res, sep=' ')


'''
두번째풀이 - 시간초과
'''
'''
for문으로 시간 추가하는거 없앰
H리스트를 단순히 높이존재여부체크 -> 시간메모용도로 용도 변경
INVENTORY = B는 B의 메모리주소 참조용도이므로 INVENTORY값 변경하면 B도바뀜
그냥 B그대로 사용해도 괜찮아서 따로 변수 설정은 안함
만약 변수가 필요하면 INVENTORY =0 하고 +B해주면됨
어찌되었든 계속 줄어든 인벤갯수가 반영되어야 하므로 변수선언 필요없음
그리고 G는 H index에 전혀 영향 안주므로 굳이 다시 reverse()할 필요 없음
그리고 못함 왜냐면 이미 sorting되서 인덱스가 망가졌기때문.
'''
# import sys
# def solution():
#     input = sys.stdin.readline
#     G = []
#     H = [0]*257 # 높이 최대 256
#     N, M, B = map(int, input().rstrip().split())
    
#     # 1차원배열G로 높이 담기
#     for _ in range(N):
#         nums = list(map(int, input().rstrip().split()))
#         for num in nums:
#             G.append(num)
    
#     # 최종으로 인벡이 뉴인벤값의 차가 0보다 작으면 그건 T에 넣지않는다. 
#     # T에 넣을땐 NT뿐만아니라 h랑 (최대합 필요없음 왜냐면 시간데이터가 비용다 말해줌)도 같이 넣어줌
#     for h in range(257):
   
#         for l in G:
                
#             if l > h:
#                 H[h] += (l - h) * 2 # 시간을 메모해줌
#                 B += (l - h)

#             if l < h:
#                 if B >= (h - l): #꺼내야하는 갯수(h-l)개가 인벤값보다 작거나 같으면
#                     H[h] += (h - l)
#                     B -= h-1

#             else:
#                     # 아예 큰값으로 표기해서 min 카운팅에 들지 못하게 막음
#                     # 인벤보다 값이 작은경우
#                     H[h] += 999999
#                     break
        
# print(solution())

'''
첫번째풀이 -시간초과
'''
# import sys
# def solution():
#     input = sys.stdin.readline
#     G = []
#     H = [0]*257 # 높이 최대 256
#     N, M, B = map(int, input().rstrip().split())
    
#     # 높이 존재여부 메모
#     for _ in range(N):
#         nums = list(map(int, input().rstrip().split()))
#         for num in nums:
#             G.append(num)
#     G.sort(reverse=True)
#     # 최종으로 인벡이 뉴인벤값의 차가 0보다 작으면 그건 T에 넣지않는다. 
#     # T에 넣을땐 NT뿐만아니라 h랑 (최대합 필요없음 왜냐면 시간데이터가 비용다 말해줌)도 같이 넣어줌
#     for h in range(257):
#         INVENTORY = B 
#         for l in G:
                
#             if l > h:
#                 H[h] += (l - h) * 2 # 시간을 메모해줌
#                 INVENTORY += (l - h)

#             if l < h:
#                 if INVENTORY >= (h - l): #꺼내야하는 갯수(h-l)개가 인벤값보다 작거나 같으면
#                     H[h] += (h - l)
#                     INVENTORY -= h-1

#                 else:
#                     # 아예 큰값으로 표기해서 min 카운팅에 들지 못하게 막음
#                     # 인벤보다 값이 작은경우
#                     H[h] += 999999
#                     break

#     return str(min(H)) + ' ' + str(H.index(min(H)))
# print(solution())