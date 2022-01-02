# 0 인덱스와 1 인덱스의 원소 교체하기
array  = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end) :
    if start >= end : # 원소가 1개인 경우 종료
        return