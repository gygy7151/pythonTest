'''
제일작은수제거하기
'''
'''
두번째풀이 -
sort하고 copy하면 2*O(N)이라서 min(arr)로 O(N)으로 줄임
'''
def solution(arr): 
    if len(arr) == 1:
        return [-1]
    MIN = min(arr)
    arr = arr[0:arr.index(MIN)] + arr[arr.index(MIN)+1:]
    return arr

'''
첫번째풀이 - 그냥 해당 인덱스 끊어서 삭제하고 대입하기
'''
# import copy
# def solution(arr): 
#     if len(arr) == 1:
#         return [-1]
#     s = copy.deepcopy(arr)
#     s.sort()
#     arr = arr[0:arr.index(s[0])] + arr[arr.index(s[0])+1:]
#     return arr
