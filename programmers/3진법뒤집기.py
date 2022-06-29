'''
예산
'''
'''
네번째풀이 - linked list로 접근하기 array보다 좀더 빨랐음
'''
def solution(n):
    answer = 0
    N = []
    
    while n:
        N.append(n % 3)
        # 반드시 정수나누기로 해주어야됨. 안그럼 소수가되고 지저분해짐.
        n = n//3
    
    # 리스트랑 문자열이랑 다름 리스트는 [start,end,**점프크기] 뱐드시 **지정해줘야됨 역정렬할때. 
    # 문자열의 경우 역순은 N[::-1]임
    N = N[-1::-1]
    
    for i in range(len(N)):
        answer += (N[i] * 3**i) 
    
    return answer 

'''
세번째 풀이 - 좀더 확장성 있는 코드 작성하려면? 그리고 메소드 이용안하려면
string arrary로 접근하기
'''
# def solution(n):
#     answer = 0
#     N = ''
    
#     while n:
#         N += str(n % 3)  
#         n = n//3
    
#     # 시간복잡도는 N이 아니다. N의 갯수는 나머지갯수이므로 O(lonN)임.
#     N = N[::-1]
    
#     for i in range(len(N)):
#         answer += (int(N[i]) * 3**i) 
    
#     return answer 


'''
두번째 풀이 - 1과2에서 런타임에러 처리
'''
# def solution(n):
    
#     if n <= 2:
#         return n
#     answer = 0

#     N = []
    
#     # 이게 좋은 코드가 아니다.. n이 1과 2이면 for문이 아예 안 움직임..
#     # 이렇게 되면 N은 빈문자열이 되므로..value 에러 뜸- > 런타임에러
#     for i in range(n//3):
#         divide = n // 3
#         left = n % 3
#         N.append(str(left))
#         n = divide

#         if n == 0:
#              break
    
#     N = "".join(N)
#     answer = int(N, 3)

#     return answer