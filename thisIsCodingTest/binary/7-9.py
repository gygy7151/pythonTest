'''
떡볶이떡 이진탐색으로 구현
'''

n, m = map(int, input().split())
slices = list(map(int, input().split()))


start = 0
end = max(slices)


while start < end :

    mid = (start + end) // 2
    result = []


    for i in range(n) :
        
        if (slices[i] -  mid) > 0 :
            
            result.append(slices[i] -  mid)
        
    if sum(result) == m :

        print(mid)
        break
        
    elif sum(result) > m :

        start = mid + 1

    else :

        end = mid - 1
        






