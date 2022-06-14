'''
음계
1부터시작
c d e f g a b C 총 8음계
ascending
descending
midxe
인지 판별
숫자는 한번씩 등장
'''
def ascend(ryric):
    for i in range(1, len(ryric)):
    
        if ryric[i] < ryric[i-1]:
            return False
    return True

def descend(ryric):
    for i in range(1, len(ryric)):
    
        if ryric[i] > ryric[i-1]:
            return False
    return True

res = ''
ryric = list(map(int, input().split()))

if abs(ryric[1] - ryric[0]) == 1:
    
    if ryric[1] > ryric[0]:
    
        if ascend(ryric):
            res = 'ascending'
    
        else:
            res = 'mixed'
    
    else: 
    
        if descend(ryric):
            res = 'descending'
    
        else:
            res = 'mixed'
else:
    res ='mixed'
print(res)


    



