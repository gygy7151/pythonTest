'''
벌집
'''
def solution(target):
    cnt = 1
    if target == 1:
        return cnt
    while True:
        res = 1 + (((cnt)*(cnt+1)*6)//2)
        cnt += 1
        if res >= target:
            return cnt
print(solution(37))
