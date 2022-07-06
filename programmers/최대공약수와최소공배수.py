'''
최대공약수와 최소공배수
'''
'''
네번째풀이 - 람다활용 함수형 프로그래밍
'''

def solution(n,m):
    gcd = lambda x,y: x if not x % y else gcd(y, x%y)
    lcm = lambda x,y: (x*y)//gcd(x,y)
    return [gcd(n,m), lcm(n,m)]
    
'''
세번째풀이 - math.lcm(), math.gcd()메소드 활용인데 이건 프로그래머스에서 막아놓음
'''
# def solution(n,m):
#     return [math.lcm(n,m), math.gcd(n,m)]
# import math


'''
두번째풀이 - 직접 유클리드호제법활용해서 구현
엇 근데 함수명 잘못되었음
최대공약수는 lcm이고
최소공배수가 gcd임..헐..
'''
# def solution(n,m):
#     ANS = []
#     def lcm(a,b):
#         while b:
#             # 아.. %나머지연산자말고 곱셉연산자를 사용해서 시간초과발생했다.
#             a, b = b, a*b
#         return a

#     def gcd(a,b):
#         res = (a*b)//lcm(a,b)
#         return res
    
#     ANS.append(lcm(n,m))
#     ANS.append(gcd(n,m))
#     return ANS
# res = solution(3, 12)
# print(res)

'''
첫번째풀이
'''
# def solution(n, m):
#     answer = []
#     def lcm(a,b):
#         while (b):
#             a, b = b, a%b
#         return a
    
#     def gcd():
#         res = (n * m) // lcm(n,m)
#         return res
#     answer.append(lcm(n,m))
#     answer.append(gcd())
#     return answer
