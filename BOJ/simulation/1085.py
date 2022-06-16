'''
직사각형에서 탈출
'''
x, y, w, h = map(int, input().split())
length = [h-y, y, w-x, x]
print(min(length))