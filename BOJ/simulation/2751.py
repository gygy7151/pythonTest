'''
수정렬하기 2

'''
'''
두번째풀이
# input()은 sys.stdin.readline보다 버퍼를 n-1배나 더 사용함
2
# 프롬프트에 글자를 입력하고 엔터를 누를때마다(데이터입력종료로 인식) 버퍼가 생기고
3
# 입력된 문자열은 해당시스템의 콘솔 입출력 인코딩을 활용해 디코딩되어 유니코드 문자열로 변환
4
# 이렇게 변환된 문자열에서 개행문자를 삭제하고 문자열을 반환하므로 시간이 상당히 오래걸림
5
# 이에 반해 sys.stdine.readline은 버퍼를 한개만 생성해서 한꺼번에 받아버리므로 상당히 빠름
6
# 단순히 개행문자를 사용자 측에서 삭제하도록 권한을 넘겼다고 해서 시간복잡도가 크게 줄었던게 아님
'''
import sys
input = sys.stdin.readline

def solution():
    N = []
    for _ in range(int(input().rstrip())):
        N.append((int(input().rstrip())))
    N.sort()
    for n in N:
        # sys.stdout.write('%d\n' %n)
        sys.stdout.write(str(n) + '\n')
solution()

'''
첫번째풀이 - 시간초과 with 병합정렬
'''
# def solution():
#     N = []
#     for _ in range(int(input())):
#         N.append(int(input()))
    
#     def merge(left, right):
#         temp = []

#         while len(left) > 0 and len(right) > 0:
#             if len(left) > 0 and len(right) > 0:
#                 if left[0] <= right[0]:
#                     temp.append(left[0])
#                 else:
#                     temp.append(right[0])
#                     right = right[1:]
#             elif len(left) > 0:
#                 temp.append(left[0])
#                 left = left[1:]
#             elif len(right) > 0:
#                 right = right[1:]

#         return temp

#     def merge_sort(list):
#         size = len(list)
        
#         if size <= 1:
#             return list
        
#         mid = len(list) // 2
#         left = merge_sort(list[:mid])
#         right = merge_sort(list[mid:])
#         merged = merge(left, right)
#         return merged

#     N = merge_sort(N)
#     print(*N, sep="\n")
        
# solution()