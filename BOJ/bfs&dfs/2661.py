'''
좋은수열
'''
import sys

def isGoodArr(arr):
    arr_len = len(arr)
    for part_len in range(1, arr_len // 2 + 1):
        for part_start in range(part_len, arr_len - part_len +1):
            if arr[part_start - part_len: part_start] == arr[part_start:part_start + part_len]:
                return False
    return True

def dfs(arr, depth):
    if depth == N:
        print("".join(list(map(str, arr))))
        sys.exit()
    arr.append(1)
    for i in range(1, 4):
        arr.pop()
        arr.append(i)
        if isGoodArr(arr):
            if not dfs(arr, depth +1):
                continue
    arr.pop()
    return False

N = int(input())
dfs([1],1)