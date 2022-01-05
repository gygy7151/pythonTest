
'''
선택정렬
'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4]

def optionSorting() :
    
    for i in range(len(array)) :

        for j in range(i + 1, len(array)) :

            if array[i] > array[j] :

                array[i], array[j] = array[j], array[i]
    
    print(array)

optionSorting()

'''
이전 예시코드
 
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :

    min_value = array[i]
    
    for j in range(i + 1, len(array)) :

        # j개의 원소배열에서 최솟값 구하기
        
        if array[i] < array[j] :

            min_value = array[i] 
        
        elif array[i] > array [j]:

            min_value = array[j]

            array[i], array[j] = array[j], array[i]
    


print(array)

'''

        
