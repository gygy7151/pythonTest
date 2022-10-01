'''
배
'''
'''
각크레인의 무게제한은 백만이하임 각 박스의 무게도 백만이하임
박스의 수는 일만이하임

어떻게 풀까?
어차피 어떤 크레인이든 1분에 한박스씩 걸리므로
박스를 크레인에 할당할때 무게제한이 큰 애들일 수록
큰 박스를 많이 할당해주는게 좋겠지?
최대한 그것도 많이?
아 근데 동시에 움직인다니깐
이거 dfs같은데..
결국 자신의 크레인에 할당된 무게제한에 젤 가까운 애들부터 pop해서
없애주어야 된다는 거네
그럼 박스를 애초에 내림차순으로 정렬해놓은 상태에서
크레인의 무게제한에 맨처음 적합한 상자가 나오면 for문을 벗어나
아 이거슨 dfs 냄새 솔솔

# 현재 남은상자 담은 배열 box - 전역변수로 관리
# 각 제한무게를 가진 크레인 별로 dfs를 돌림
# 단 dfs 파라미터는 제한 무게와 time을 0으로 넣음
# 만약 옮길 수 있는 화물이 있으면 time + 1해주고 다시 dfs돌림
# 옮길 수 있는 화물이 아예 0이면 time을 그대로 리턴함
# 각 dfs가 최종 리턴한 값을 answer랑 비교해서 answer보다 작으면 result값을 answer에 대입
# answer를 출력한다.
'''
'''
네번째풀이 - 이진탐색으로 시간해결함
'''
import sys
from bisect import *
input = sys.stdin.readline
def solution():
    N = int(input())
    crane = list(map(int, input().split()))
    M = int(input())

    def bfs():
        box = list(map(int, input().split()))

        # 아..박스는 오름차순이어야 되네 그래야 이분탐색이 되나봄..
        # 그렇지 이진 탐색은 정렬된 배열일때만 가능하지!!!!!!!
        box.sort()
        crane.sort(reverse=True)

        if box[-1] > crane[0]:
            return -1

        time = 0
        while box:
            
            for limit in crane:
                max_val = bisect(box, limit)
                # 삭제된 경우도 존재하기 때문에 box가 있는지부터 체크해줘야됨
                if box and box[max_val-1] <= limit:
                    box.pop(max_val-1)
            
            time += 1
            
        return time
    
    print(bfs())
solution()



'''
세번째풀이 - 시간초과남
'''
# import sys
# input = sys.stdin.readline
# def solution():
#     N = int(input())
#     crane = list(map(int, input().split()))
#     M = int(input())

#     def bfs():
#         box = list(map(int, input().split()))
#         box.sort(reverse=True)
#         crane.sort(reverse=True)
#         time = 0

#         if box[0] > crane[0]:
#             return -1

#         while box:

#             for crane_limit in crane:
#                 for weight in box:
#                     if weight <= crane_limit:
#                         box.remove(weight)
#                         break
            
#             time +=1

#         return time
    
#     print(bfs())
# solution()
    



'''
두번째풀이 - bfs로 풀어보려면 어케해야하나?
참조 : https://jokerldg.github.io/algorithm/2021/06/11/ship.html
1. 박스랑 크레인 제한무게 모두 내림차순으로 하고
2. 박스제일 큰값이 크레인보다 젤 크면 옮길 수 없으므로 -1 출력해야됨 -> 아.. 이부분 놓쳣다.
3. 크레인 제한무게 차례로 돌면서 box가 해당 크레인 제한무게보다 작거나 같으면 box.remove(limit) 해준후 break 한다.
4. 크레인 for문 다돌면 time += 1 해준다.
5. while문으로 box가 있을때까지 반복해준다.
6. time을 출력해주면 끝!
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N = int(input())
#     crane = list(map(int, input().split()))
#     M = int(input())
#     box = list(map(int, input().split()))
#     #1. 박스랑 크레인 제한무게 모두 내림차순정렬
#     crane.sort(reverse=True)
#     box.sort(reverse=True)

#     #2. 박스제일 큰값이 크레인보다 젤 크면 옮길 수 없으므로 -1 출력
#     if box[0] > crane[0]:
#         print(-1)
#         return

#     #3. 크레인 제한무게 차례로 돈다.
#     time = 0
#     while box:
        
#         # [실수] box에 값이 없으면 break해줘야됨
#         if not box:
#             break

#         # 아... 삭제할땐 인덱스로 접근할께 아니라 존재하는걸 실시간 반영하도록
#         # for crane_limit in crane:
#         #     for weight in box: ->  이런식으로 접근해야 했었구나..!
#         # 이렇게 하면 dfs도 bfs로 구현이 가능한거구나.. 재영이가 말한게 이거구나..
#         for i in range(N):
#             for j in range(M):
#                 print(box[j])
#                 print(crane[i])
#                 print('*'*50)
#                 #4. box가 해당 크레인 제한무게보다 작거나 같으면 box.remove(limit) 해준후 break 한다.
#                 if box[j] <= crane[i]:
#                     box.remove(box[j])
#                     break
        
#         #5. 크레인 for문 다돌면 time += 1 해준다.                    
#         time += 1
    
#     print(time)

# solution()
'''
첫번째풀이 - 뎁스초과
'''
# def solution():
#     N = int(input())
#     crane = list(map(int, input().split()))
#     M = int(input())
#     box = list(map(int, input().split()))
#     box.sort(reverse=True)

#     def dfs(limit, time):
#         # 삭제된 박스의 갯수가 총 박스갯수와 같은 경우
#         if box.count(0) == M:
#             return time
#         # 무게가 더 나가면 안되는거지
#         # 젤 작은 무게조차 제한무게보다 크면 더이상 옮길게 없는경우임
#         min_val = min(box)
#         if min_val > limit:
#             return time
#         else:
#             # box에 해당 요소에 0을 대입해준다.
#             # box무게는 0보다 크고 백만보다 같거나 작은 범위의 자연수이므로 0을 대입해도 비교할때 상관없다.
#             max_idx = box.index(max(box))
#             box[max_idx] = 0
            
#             dfs(limit, time+1)
#             return
        
    
#     # 박스를 옮기는 최소시간 answer
#     answer = int(1e9)
#     for i in range(N):
#         res = dfs(crane[i], 0)
#         if res < answer:
#             answer = res
    
#     print(answer)
# solution()

