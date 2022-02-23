'''
메모이제이션기법활용한 피보나치수열
#탑다운방식은 재귀함수활용
'''
d = [0] * (100)

def dp(x):
    if x == 1:
        return 1
    if x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = dp(x-1) + dp(x-2)
    return d[x]

result = dp(30)
print(result)

