'''
곱셈
'''
'''
세번째
'''
def solution():
    a, b, c = map(int, input().split())

    def recur(a,b):
        if b == 0: return 1
        x = recur(a, b//2)

        if b % 2 == 0:
            return x * x % c
        else:
            return x * x * a % c
    
    print(recur(a,b))
solution()

'''
두번쨒 
'''
a, b, c = map(int, input().split())

def sol(a,b):
    if b == 1:
        return a % c
    
    temp = sol(a, b// 2)

    if b % 2 == 0:
        return temp * temp % c
    
    else:
        return temp * temp * a % c

print(sol(a,b))

'''
첫번째

'''
# a, b, c = map(int, input().split())
# for _ in range(int(b**0.5)):
#     a *= a
# print(a % c)