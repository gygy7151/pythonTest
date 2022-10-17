'''
백준 수 묶기
'''
'''
두번째풀이
- 둘중 하나가 1인경우에는 곱하지말고 더하셈
- 그리고 굳이 음수랑 양수랑 같이 계산할 필요없었음
'''
import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    minus = []
    plus = []

    for _ in range(N):
        a = int(input())

        if a <= 0: minus.append(a)
        else: plus.append(a)

    #아..오른쪽부터 pop해서 minus를 내림차순으로 해주었던 거구나! 제일 작은것부터 pop하려고!
    minus.sort(reverse=True)
    plus.sort()
    
    ans = 0

    while len(plus) >= 2:
        a = plus.pop()
        b = plus.pop()

        if a == 1 or b == 1:
            ans += a + b
        
        else:
            ans += a * b
        
    
    if plus:
        ans += plus.pop()
    
    while len(minus) >= 2:
        
        a = minus.pop()
        b = minus.pop()
        ans += a * b

    
    if minus:
        ans += minus.pop()
    
    print(ans)
solution()

        







'''
첫번째풀이 -  틀림
'''
# import sys
# input = sys.stdin.readline

# def solution():
#     N = int(input())

#     minus = []
#     plus = []

#     for _ in range(N):
#         a = int(input())

#         if a < 0: minus.append(a)

#         else: plus.append(a)
    
#     # 음수는 오름차순, 양수는 내림차순으로 숫자 정렬한다.
#     plus.sort(reverse=True)
#     minus.sort()
    
#     result = 0
    
#     if len(minus) >= len(plus):
#         while plus:
#             p_num = plus.pop(0)
#             m_num = minus.pop(0)
#             result += (p_num + m_num)
        
#         if minus:

#             for m_idx in range(0, len(minus)-1, 2):
#                 result += minus[m_idx] * minus[m_idx+1]
    
#     else:
#         while minus:
#             p_num = plus.pop(0)
#             m_num = minus.pop(0)
#             result += (p_num + m_num)

#         for p_idx in range(0, len(minus)-1, 2):
#             result += plus[p_idx] * plus[p_idx+1]

    
#     print(result)
# solution()



    


    