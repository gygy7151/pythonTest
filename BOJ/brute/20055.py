'''
컨베이어벨트 위의 로봇 
'''

def check(s,k):
    count = 0
    for e in s:
        if e == 0:
            count += 1
    if count == k:
        print('k가 되었당')
        return True
    else:
        return False

def move(n):
    global strength
    global box_bot
    for i in range(2*n):
        if i == ((2*n)-1):
            box_bot[i] = False
            continue
        if strength[i+1] >= 1 and not box_bot[i+1]:
            box_bot[i] = False
            box_bot[i+1] = True
            strength[i+1] -= 1

n, k = map(int, input().split())
strength = list(map(int, input().split()))
count = 0
box_bot = [False] * (2*n)
find = False
while True:
    if strength[0] >= 1:
        count += 1
        strength[0] -= 1
        box_bot[0] = True
        move(n)
    if check(strength,k):
        find = True
        break
    if find:
        break