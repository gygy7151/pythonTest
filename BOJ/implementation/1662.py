'''
압축
'''
'''
첫번째풀이
'''
'''
K는 한자리 정수이고
Q는 0자리 이상의 문자열
K(K(K(Q)))
Q라는 문자열이 K번 반복되는 거임
아.. 
와 이거 되게 어렵다..
'''
def solution():
    S = input()
    stack =[]
    length = 0
    K = ''

    for char in S:
        if char.isdigit():
            length += 1
            K = char # 가장 최근의 반복되는 수
        
        elif char == '(':
            # K는 곱해야 하는 수, length-1은 (를 만나기 전까지의 전체길이
            stack.append((K, length-1))

            length = 0 # 반드시 초기화 해줘야됨 ()가 또 나올 수 있으므로

        else:
            # )일때, 곱해야하는 수 multi, '('이전부터 multi 전까지의 길이 preL
            # ( ) 사이에 있는 문자길이 length
            multi, preL = stack.pop()

            length = (int(multi) * length) + preL

    print(length)
solution()

'''
순열의 순서
'''
'''
첫번째풀이 - 메모리 초과..?
permuation 모듈 사용해야될꺼 같음.
K번째 수열을 나타내는 N개의 수를 출력하거나
몇번째 수열인지를 출력해야한다.
'''
from itertools import permutations
import bisect

def solution():
    N = int(input())
    # 순열을 정렬시킴
    SET = list(permutations(range(1,N+1), N))
    
    # 순열 정렬은 첫번째수가 작은것 > 두번째수가 작은것 > 세번째수 작은것
    SET.sort(key= lambda x:(x[0], x[1], x[2]))

    case = list(map(int, input()))
    # 소문제 번호가 1인 경우
    if case[0] == 1:
        ## K를 입력 받음 1개
        ## K번째 순열을 그대로 출력하면 됨
        print(*SET[case[1]])
    
    # 소문제 번호가 2인 경우
    else:
        ## 임의의 N개의 수열 즉1부터 N+1개까지 인덱스로 잡으면 됨
        temp = case[1:]
        ## 해달 수열이 미리 구해놓은 수열에 해당하는 걸 찾으면 끝!
        ## 이때 이분탐색 bisect을 활용할것
        print(bisect.bisect_left(temp))
solution()



