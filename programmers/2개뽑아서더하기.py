
'''
2개뽑아서더하기
'''
'''
세번째풀이 - 인덱스 에러가 발생했다.
'''
def solution(numbers):
    answer = []
    N = len(numbers)
    # numbers안의 요소는 최대 100이하이므로 100+100 = 200까지의 인덱스범위를 지정한다.
    MEMO = [0] * (201)

    for i in range(N):
        for j in range(i+1,N):
            NN = numbers[i] + numbers[j]
            if MEMO[NN] == 0:
                MEMO[NN] = 1

    for n in range(len(MEMO)):
        if MEMO[n] == 1:
            answer.append(n)
    return answer


'''
두번째 풀이 
- 굳이 역정렬 할필요 없었다.
- 중복되지 않는걸 검사한다한들 완전히 오름차순으로 값이 들어가지도 않는다.
- 결론은 그냥 두개씩 set으로 중복 없애는게 제일 깔끔함
- 아니면 memo한걸 기반으로 1인경우만 출력하던가 -> 이러면 sort할 필요없음
insert는 O(N)임. 맨첫번째에 요소를 집어넣는다해도 뒤에 요소가 밀리기때문
그래서 맨뒤에 append해주는게 젤 좋음
위 내용 반영해서 다시 작성함
'''
# def solution(numbers):
#     answer = []
#     N = len(numbers)
#     MEMO = [0] * (numbers[0]+numbers[1]+1)

#     for i in range(N):
#         for j in range(i+1,N):
#             NN = numbers[i] + numbers[j]
#             if MEMO[NN] == 0:
#                 MEMO[NN] = 1

#     for n in range(len(MEMO)):
#         if MEMO[n] == 1:
#             answer.append(n)
#     return answer

'''
첫번째 풀이
'''
# def solution(numbers):
#     answer = []
#     N = len(numbers)
#     numbers.sort(reverse=True)
#     MEMO = [0] * (numbers[0]+numbers[1]+1)

#     for i in range(N):
#         for j in range(i+1,N):
#             NN = numbers[i] + numbers[j]
#             if MEMO[NN] == 0:
#                 MEMO[NN] = 1
#                 answer.insert(0, NN)
#     print(answer)
#     answer.sort()
#     return answer