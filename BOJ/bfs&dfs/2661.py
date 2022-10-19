'''
좋은수열
'''
'''
네번째/다섯번째풀이 - 모든경우를 백트래킹 하는거임
1부터 시작, 숫자 하나씩 붙여가며 좋은 수열인지 판단하는 방법으로
if elif elif를 사용하지 않음.
그리고 좋은 수열인지 판단하는 조건 부분은 다른 코드 참고햇음.
'''
import sys
def solution():
    N = int(input())

    def check(arr):
        M = len(arr)
        for i in range(1, M // 2 + 1):
            leng = i
            start = 0
            start2 = start + i
            for j in range(M - (leng * 2)+ 1):
                if arr[start + j : start + j + leng] == arr[start2 + j : start2 + j + leng]:
                    return False

        return True
    
    def dfs(arr):
        #if문 여러개보다 그냥 우선 dfs에 넣어주고 초기에 체크해주는게 효율적
        if check(arr) is False:
            return
        if len(arr) == N:
            print(arr)
            #아.. 이게 맨처음 제일 작은값 구해지면 dfs뿐만아니라 solution함수 전체를 종료시키는 강려크한 코드구나.
            sys.exit()
            return
        
        else:
            dfs(arr+'1')
            dfs(arr+'2')
            dfs(arr+'3')

    
    if N == 1:
        print(1)
        return
    #1로시작
    else:
        dfs('1')

solution()



'''
세번째풀이- 청크 비교하는 부분이 틀렸음
모든 칸마다 요소 다 비교해주어야되었는데 절반만 확인해서 틀린거임.
'''
# import heapq
# import sys

# def solution():
#     N = int(input())

#     def check(arr):
#         M = len(arr)
#         for i in range(M-1, len(arr)//2+1, -1):
#             # 비교하는 청크길이가 수열길이를 벗어나면 예외처리 해준다.
#             if i < 0 or i - (M - i) < 0:
#                 continue
#             chunkA = arr[i:M]
#             chunkB = arr[i - (M-i): M - (M-i)]

#             if chunkA == chunkB:
#                 return False

#         return True
    
#     def dfs(arr):
#         if check(arr) is False:
#             return
        
#         if len(arr) == N:
#             print(arr)
#             sys.exit()

#         dfs(arr+'1')
#         dfs(arr+'2')
#         dfs(arr+'3')

    
#     if N == 1:
#         print(1)
#         return
#     #1로시작
#     else:
#         dfs('1')
    
# solution()


'''
두번째풀이 - 틀림.
아.. 연속해서 인접한 두개의 부분 수열이 존재하면 나쁜 수열이였다..
'''
# from itertools import product

# def solution():
#     N = int(input())
#     # 좋은 수열 샘플 담은 배열 good
#     good = []

#     def check(chunk):
#         for num_idx in range(N):
#                 if number[num_idx:idx] == chunk:
#                     return False

#         return True
#     # 중복순열을 구한다
#     arr = [1,2,3]
#     sets = list(product(arr, repeat = N))

#     for num in sets:
#         # 좋은 수열 찾기 위한 샘플 수열 number
#         number = list(map(int, num))

#         for idx in range(1,N+1):
#             chunk = number[0:idx]
#             if not check(chunk):
#                 break
        
#         else:
#             # 중복검열에 통과한 경우 좋은 수열에 추가한다.
#             good.append(num)
    

#     # 좋은 수열을 오름차순 정렬한다.
#     good.sort()
#     print(good[0])

# solution()

            
        



    


'''
첫번째풀이
'''
# import sys

# def isGoodArr(arr):
#     arr_len = len(arr)
#     for part_len in range(1, arr_len // 2 + 1):
#         for part_start in range(part_len, arr_len - part_len +1):
#             if arr[part_start - part_len: part_start] == arr[part_start:part_start + part_len]:
#                 return False
#     return True

# def dfs(arr, depth):
#     if depth == N:
#         print("".join(list(map(str, arr))))
#         sys.exit()
#     arr.append(1)
#     for i in range(1, 4):
#         arr.pop()
#         arr.append(i)
#         if isGoodArr(arr):
#             if not dfs(arr, depth +1):
#                 continue
#     arr.pop()
#     return False

# N = int(input())
# dfs([1],1)