'''
도서관
'''
'''
첫번째풀이
'''

# 문제조건에선 책을 모두 제자리에 놔둔 후엔 다시 제자리로 돌아올 필요가 없기 때문에 
# 제일 큰 값에 대해서만 예외처리를 해주면 된다

# minus 리스트에서 m으로 나눠지는 인덱스들, len(minus)%m >0 이라면 가장 끝에 있는 값 -> count리스트에 삽입
# plus 리스트에서 m으로 나눠지는 인덱스들, len(plus)%m >0 이라면 가장 끝에 있는 값 -> count리스트에 삽입
# 이후 count 오름차순 정렬한다음 가장 큰 값 하나만 한번만 더하고 나머지 값에 대해서는 합한 후 2배해주면 된다.

def solution():
    N, M = map(int, input().split())
    locationBook = list(map(int, input().split()))

    plus = []
    minus = []
    max_value = 0
    answer = 0

    # 음수부분과 양수부분을 나눈다.
    # 음수부분 -> minus 리스트에 abs() 절대값을 씌워준후 내림차순 정렬
    # 양수부분 -> plus 리스트에 내림차순 정렬
    for location in locationBook:
        if location > 0:
            plus.append(location)
        
        else:
            minus.append(location)
        
        if abs(location) > abs(max_value):
            max_value = location
    
    plus.sort(reverse=True)
    # 음수의 경우 오름차순에 절대값으로 변경하면 내림차순 정렬과 가음
    minus.sort()

    distance = []

    # 0-indexex로 시작하므로, M개씩 이동하면 새로운 묶음의 절대값 가장 큰수를 선택하게됨
    # 이부분이 헷갈려서 코드 작성때 어려웠음.
    for i in range(0, len(plus), M):
        if plus[i] != max_value:
            distance.append(plus[i])

    for i in range(0, len(minus), M):
        if minus[i] != max_value:
            distance.append(minus[i])

    # 그리고 초기에 맨처음 가장 큰값 구해줌 어차피 편도값만 더해주면됨. 안돌아외도되니깐.
    answer = abs(max_value)

    for i in distance:
        answer += abs(i *2)

    print(answer)
solution()
