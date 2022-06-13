'''
상수
'''
A, B = map(int, input().split())
A, B = list(str(A)), list(str(B))
A, B = A[-1::-1], B[-1::-1]
A, B = ''.join(A), ''.join(B)
if int(A) > int(B):
    print(int(A))
else:
    print(int(B))