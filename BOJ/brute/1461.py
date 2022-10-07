'''
도서관
'''
'''
두번째풀이
'''
'''
만약 M개라는 조건이 없다면?
만약 N이 100만이 된다면? 시간복잡도는? 
'''
# 음수, 양수로 나누되, N의 값의 범위를 참고해 max_val 기초값을 설정하고 비교하면서 갱신해줌
# 근데 어차피..sort를 해야되네 퀵정렬은 O(NlogN)인데 여기선 (N/Klog N/K)가 되겠군 다른 하나는 (KlogK)
# 
# 문제조건에선 책을 모두 제자리에 놔둔 후엔 다시 제자리로 돌아올 필요가 없기 때문에 
# 제일 큰 값에 대해서만 예외처리를 해주면 된다
 # 시간복잡도 O[N]-> O[N/KlogN/K]로 개선했다고 생각했는데 4ms나 더 걸렸넹 ..

def solution():
    N, M = map(int, input().split())
    locationBook = list(map(int, input().split()))

    plus = []
    minus = []
    # 제일 멀리 있는 책의 위치
    max_walk = 0

    # 양수와 음수를 나눈다.
    for location in locationBook:
        if location > 0:
            plus.append(location)
        
        else:
            minus.append(location)
        
        # 마지막 책은 제일 먼 걸음에 있는 책으로 정한다
        # 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요 없기때문
        if abs(location) > abs(max_walk):
            max_walk = location
    
    # 양수는 내림차순으로 음수는 오름차순으로 정렬한다
    plus.sort(reverse=True)
    minus.sort()

    #최소 걸음 수
    min_walk_num = 0

    #첫번째풀이와 다르게 리스트가 아닌 숫자로 계산하여 공간복잡도 낮춤
    
    # M권을 들고 양수 방향에 책을 모두 제자리에 놔둔다.
    for i in range(0, len(plus), M):
        # 제일 멀리 있는 책은 무시한다
        if plus[i] != max_walk:
            min_walk_num += plus[i]
    
    # M권을 들고 음수 방향에 책으 모두 제자리에 놔둔다.
    for i in range(0, len(minus), M):
        if minus[i] != max_walk:
            # 최소걸음 수를 계산하기 위해 절대값으로 바꿔 더한다.
            min_walk_num += abs(minus[i])
    

    # 그리고 초기에 맨처음 가장 큰값 더해줌 어차피 편도값만 더해주면됨. 안돌아외도되니깐.
    # 첫번째 풀이와 다르게 for문을 사용하지 않아서 좋음.
    
    # 최소 걸음수는 책의 제자리 위치와 현재 책의 위치를 왕복하여 계산한다.
    min_walk_num *= 2
    # 최소걸음수를 계산하기 위해 절대값으로 제일 멀리있는 책의 거리를 더한다. (음수일지 양수일지 모르는일.....)
    min_walk_num += abs(max_walk)

    print(min_walk_num)

solution()



'''
첫번째풀이
'''

# # 문제조건에선 책을 모두 제자리에 놔둔 후엔 다시 제자리로 돌아올 필요가 없기 때문에 
# # 제일 큰 값에 대해서만 예외처리를 해주면 된다

# def solution():
#     N, M = map(int, input().split())
#     locationBook = list(map(int, input().split()))

#     plus = []
#     minus = []
#     max_value = 0
#     answer = 0

#     # 음수부분과 양수부분을 나눈다.
#     # 음수부분 -> minus 리스트에 abs() 절대값을 씌워준후 내림차순 정렬
#     # 양수부분 -> plus 리스트에 내림차순 정렬
#     for location in locationBook:
#         if location > 0:
#             plus.append(location)
        
#         else:
#             minus.append(location)
        
#         if abs(location) > abs(max_value):
#             max_value = location
    
#     plus.sort(reverse=True)
#     # 음수의 경우 오름차순에 절대값으로 변경하면 내림차순 정렬과 같음
#     minus.sort()

#     distance = []

#     # 0-indexex로 시작하므로, M개씩 이동하면 새로운 묶음의 절대값 가장 큰수를 선택하게됨
#     # 이부분이 헷갈려서 코드 작성때 어려웠음.
#     for i in range(0, len(plus), M):
#         if plus[i] != max_value:
#             distance.append(plus[i])

#     for i in range(0, len(minus), M):
#         if minus[i] != max_value:
#             distance.append(minus[i])

#     # 그리고 초기에 맨처음 가장 큰값 구해줌 어차피 편도값만 더해주면됨. 안돌아외도되니깐.
#     answer = abs(max_value)

#     for i in distance:
#         answer += abs(i *2)

#     print(answer)
# solution()
