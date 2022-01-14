import random
import sys
#재귀호출 뎁스 확장하는 라이브러리
sys.setrecursionlimit(10**7)
'''
랜덤하게 피봇추출하여 정렬한 퀵정렬
=> 시간복잡도 가장 낮추는 방법

'''

array  = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


pivot_idx = round(random.uniform(0, len(array)-1))
print(pivot_idx)

array[0], array[pivot_idx] = array[pivot_idx], array[0]
print(array)
print('랜덤 피봇 맨 앞으로 이동완료')

def quick_sort(array ,start ,end) :

    print(start, end, '출발 및 끝점')
    if end <= start :
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right :

        while left <= end and array[left] <= array[pivot] :
            left += 1


        #호어정렬이므로 피봇과 인덱스가 같으면 안됨
        while right > start and array[right] >= array[pivot] :
            right -= 1


        if left > right : 

            array[right], array[pivot] = array[pivot], array[right]

        else :
            
            array[left], array[right] = array[right], array[left]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
    

