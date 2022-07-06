'''
직사각형 별찍기
'''
'''
두번째풀이
'''
n, m = map(int, input().strip().rsplit())
print((('*')*n + '\n')*m)


'''
첫번째풀이
# '''
# n, m = map(int, input().strip().split())

# stars = ['*'] * n
# stars = ''.join(stars)
# for _ in range(m):
#     print(stars)
