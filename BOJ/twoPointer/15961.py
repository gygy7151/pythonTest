'''
회전초밥
'''
'''
다섯번째풀이 - 투포인터
'''
import sys
input = sys.stdin.readline
def solution():
    N, d, k, c = map(int, input().split())
    sushi = [int(input()) for _ in range(N)]
    sushi.extend(sushi[0:k])
    eat = [0] * (d+1)

    ans = 0
    cur = 1
    # 쿠폰스시는 미리 먹은걸로 체크
    eat[c] += 1

    for i in range(k):
        eat[sushi[i]] += 1

        # 1더하기 전에 0이었으므로 처음 집는 스시종류
        if eat[sushi[i]] == 1:
            cur += 1
    
    #임시로 초기 비교값 담는용도
    ans = cur
    print(cur)
    # 스시번호 종류는 1번부터 시작임..그래서 위에 eat +1
    # 대신 맨첫번째 구간은 미리 구해놓았기 때문에 1번부터 시작하는거임
    for i in range(1, N+1):
        left = i-1
        right = i-1+k

        eat[sushi[left]] -= 1
        # 0보다 작거나 같으면 모두 -1 해주면됨
        if eat[sushi[left]] ==0 :
            print('삐짐')
            cur -= 1

        eat[sushi[right]] += 1
        print(sushi[right])
        if eat[sushi[right]] ==1:
            print('넣음')
            cur += 1

        print(cur)
        if ans < cur:
            ans = cur
    
    print(ans)

solution()








'''
네번째풀이 - 투포인터 -틀림
'''

# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# def solution():
#     N, d, k, c = map(int, input().split())
#     sushi = [int(input()) for _ in range(N)]
#     howManyEat = defaultdict(int) # 초밥종류가 인덱스가 됨

#     defaulCnt = 1
#     for i in range(k):
#         howManyEat[sushi[i]] += 1
#         if howManyEat[sushi[i]] == 1:
#             defaulCnt += 1

#     selectSushiCnt = defaulCnt # +1은 쿠폰초밥
    
#     for i in range(1,N):
#         howManyEat[sushi[i]] -= 1
#         if howManyEat[sushi[i]] == 0:
#             selectSushiCnt -= 1

        
#         howManyEat[sushi[(i+k-1)%N]] += 1
#         if howManyEat[sushi[(i+k-1)%N]] == 1: #처음 카운팅하는 가짓수라면 1이고 아니면 1보다 큰값이므로 중복예외처리기능
#             selectSushiCnt += 1
        
#         selectSushiCnt = max(selectSushiCnt, defaulCnt)
    
#     print(selectSushiCnt)
        
# solution()

        


'''
세번째풀이 - 시간초과.. 굳이 안먹는 스시를 삭제한느 연산은 불필요햇음
'''
# import sys
# from collections import defaultdict, deque
# input = sys.stdin.readline

# def solution():
#     N, d, k, c = map(int, input().split())

#     #회전대
#     window = deque()
#     for _ in range(N):
#         window.append(int(input()))
    
#     #회전대연장
#     window.extend(window)

#     selectSushi = defaultdict(int)

#     #k개 먼저 먹기
#     for i in range(k):
#         selectSushi[window[i]] += 1
    
#     #쿠폰스시도 먼저 먹고들어가기
#     selectSushi[c] += 1

#     result = 0
#     for i in range(N):
#         result = max(result, len(selectSushi))

#         #왼쪽꺼 없애기
#         selectSushi[window[i]] -= 1
#         if selectSushi[window[i]] == 0:
#             window.popleft()
#         #오른쪽꺼 더하기
#         selectSushi[window[i+k-1]] += 1
#         print(selectSushi)
    
#     print(result)


# solution()

'''
두번째풀이 - 슬라이딩 윈도우, defaultdict사용 - 시간초과
'''
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# def solution():
#     n, d, k, c = map(int, input().split())
#     # 회전대
#     window = [ int(input()) for _ in range(n)]
#     window.extend(window) #원형이라 2개를 이어준다
#     left = 0
#     right = 0
#     isEatSushi = defaultdict(int)
#     result = 0

#     # 쿠폰번호 초밥은 무조건 먹고 들어감
#     isEatSushi[c] += 1

#     # 처음엔 k구간만큼 먹기
#     while right < k:
#         isEatSushi[window[right]] += 1
#         right += 1

#     # 슬라이딩 윈도우 적용
#     while right < len(window):
#         result = max(result, len(isEatSushi))

#         #맨 왼쪽 초밥제거
#         isEatSushi[window[left]] -= 1
#         if isEatSushi[window[left]] == 0:
#             del isEatSushi[window[left]]

#         #오른쪽 초밥 추가하기
#         isEatSushi[window[right]] += 1

#         left += 1
#         right += 1
    
#     print(result)

# solution()

'''
첫번째 풀이 - 선형탐색 시간초과
'''
# import sys
# input = sys.stdin.readline
# import heapq
# def solution():
#     N, D, K, C = map(int, input().split())
#     sushi = [int(input()) for _ in range(N)]
#     sushi += sushi[0:K-1]
#     answer = set()
#     for i in range(N):
#         if len(sushi[i:i+K]) +  1 not in answer:
#             answer.add(len(set(sushi[i:i+K])) +  1)
    
#     print(max(answer))

# solution()