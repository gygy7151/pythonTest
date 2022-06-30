'''
소트인사이드
'''
def solution():

    S = list(input())
    S.sort(reverse=True)
    return S

res = solution()
print(*res, sep="")