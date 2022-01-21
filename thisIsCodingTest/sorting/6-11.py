'''
성적이 낮은 순으로 학생 출력하기
학생 정보는 학생의 성적과 이름으로 구분
'''
import random

n = int(input())
arr = []

for i in range(n) :

    arr.append(list(map(str, input().split())))

print(arr, '초기')

def quick_sort(arr, start, end) :

    pivot = start
    left = start + 1
    right = end

    while left <= right :

            while left <= end and arr[left][1] < arr[pivot][1] :

                left += 1

            while right > start and arr[right][1] > arr[pivot][1] :

                right -= 1

            if left > right :

                arr[right], arr[pivot] = arr[pivot], arr[right]
            
            else :

                arr[right], arr[left] = arr[right], arr[left]
        
            quick_sort(arr, start, right -1)
            quick_sort(arr, right+1, end)
    
quick_sort(arr, 0, len(arr)-1)

print(arr, 'end')

result =[]
for i in range(n) :

    print(i)
    result.append(arr[i][0])

#리스트 한줄에 출력하기
print(' '.join(result))




