'''
최대공약수와 최소공배수 
'''
'''
두번째풀이 - 유클리드호제법 활용
호제법이란 두수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘
2개의 자연수 a,b에 대해 a를 b로 나눈 나머지를 r이라하면,
a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다.
최소공배수는 a,b의 곱을 a,b의 최대 공약수로 나누면 나오게된다.
'''

def solution(A,B):

    #최대공약수(Greast Common Factor)
    def gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    #최소공배수(Least Common Multiple)
    def lcm(a,b):
        return a * b // gcd(a,b)
    
    a = gcd(A,B)
    b = lcm(A,B)
    print(a)
    print(b)
    
A, B = map(int, input().split())
solution(A,B)



'''
첫번째풀이- 1000부터 이상하게 구해짐..
'''
# def solution(A,B):
#     MAX_C_N = 0
#     if A == 1 or B == 1:
#         MAX_C_N = 1

#     else:
#         #최대공약수구하기
#         for i in range(2, ((A+B)//2)+1):
#             if A % i == 0 and B % i == 0:
#                 MAX_C_N = i

#     print(MAX_C_N)

#     MIN_C_N = MAX_C_N
#     #최소공배수구하기
#     while True:
        
#         if MIN_C_N % A == 0 and MIN_C_N % B == 0:
#             print(MIN_C_N)
#             break
        
#         else:
#             MIN_C_N += MAX_C_N

# A, B = map(int, input().split())
# solution(A,B)