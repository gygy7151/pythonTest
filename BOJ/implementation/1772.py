'''
순열의 순서
'''
'''
두번째풀이 - 아..애초에 20!이 매우매우 큰수라서 안되나봄..
사용한 알고리즘 : dfs

참조 : https://deok2kim.tistory.com/102
'''
import math

def solution():
    N = int(input())
    data = list(map(int, input().split()))
    case = data[0]

    # 소문제 1
    if case == 1:
        K = data[1]
        numbers = [x for x in range(N+1)]
        answer = []

        def find_arr(n,k):
            nonlocal answer
            if len(answer) == N - 1:
                answer.append(numbers[-1])
                return

            case = math.factorial(n) // n
            sequence = math.ceil(k / case) #올림 1.16은 2가됨
            answer.append(numbers.pop(sequence))

            find_arr(n-1, k-(case * (sequence-1))) #그치 반드시 sequence에 -1해줘야됨
        find_arr(N, K)
        print(*answer)

    # 소문제 2
    else:
        K = data[1:]
        numbers = [x for x in range(1, N+1)]
        answer = []

        def find_k():
            n = N

            for num in K:
                # N!//N을 담는 용도인 case
                case = math.factorial(n) // n
                # K순열의 숫자 num의 idx
                idx = numbers.index(num)

                if len(numbers) == 2:
                    idx += 1
                    answer.append(case*idx)
                    return
                numbers.pop(idx)
                # 해당인덱스만큼 N!//N을 곱해주면 최소 몇번째에 뒤에 있는지 알 수 있음
                answer.append(case*idx)
                n -= 1

        find_k()
        print(sum(answer))

solution()

'''
첫번째풀이 - 4% 메모리 초과..?
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
        print(bisect.bisect_left(SET,temp))
solution()



