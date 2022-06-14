'''
알람시계

주의>
시간이 0시일때
주어진 분 - 45이 0보다 크거나 같을때
주어진 분 - 45이 0보다 작을때
'''
H, M = map(int, input().split())
if M - 45 < 0:
    if H - 1 < 0:
        H = 23
    else:
        H -= 1
    M = 60 + (M - 45)
else:
    M -= 45
print(H,M,sep= ' ')

