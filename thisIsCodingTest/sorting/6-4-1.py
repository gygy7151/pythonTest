'''
호어 퀵정렬

사고관점 : 인덱스는 변하지 않고, 인덱스 요소값만 변화한다.
'''
array  = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if end <= start :
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right :

        while left <= end and array[left] <= array[pivot] :
            left += 1

        while right > start and array[right] >= array[pivot] :
            right -= 1
        
        if left > right :

            array[right], array[pivot] = array[pivot], array[right]
        
        else :
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end) 

            
quick_sort(array, 0, len(array) -1)
print(array)
    