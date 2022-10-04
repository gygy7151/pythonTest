'''
줄어드는 수
'''
'''
두번째풀이 - 30%에서 틀림
'''
from itertools import combinations

def solution():
    n = int(input())
    nums = []

    for i in range(1, 11):
        # 0부터 9까지 구해주어야됨
        # 아..0,10인데 1,10이라고 했구나
        for comb in combinations(range(1,10), i):
            comb = list(comb)
            comb.sort(reverse=True)
            nums.append(int("".join(map(str, comb))))
    
    nums.sort()

    # 아..문제를 잘못해석했다.
    # 0번째를 1번째로
    try:
        print(nums[n-1])

    except:
        print(-1)
solution()



'''
첫번째풀이 - 40%에서 틀림..
'''
'''
100만 곱하기 100만까지 MAX로 잡음
'''
from itertools import combinations

N = int(input())
# defaultdict 초기값 잘 설정해주자.
nums = list()

for i in range(1, 11):
    for comb in combinations(range(0,10), i):
        temp = list(comb)
        temp.sort(reverse=True)
        nums.append(int("".join(map(str, temp))))
        

nums.sort()

try:
    print(nums[N-1])

except:
    print(-1)


'''
세번째풀이
'''

import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list() # 모든 감소하는 수

for i in range(1, 11):      #  1~10개의 조합 만들기 (0~9개니깐)
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순

try:
    print(nums[n - 1])
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)

import sys
from itertools import combinations

N = int(input())

nums = list()

for i in range(1, 11):
    for comb in combinations(range(0,10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        comb.append(int("".join(map(str, comb))))
        

nums.sort()

try:
    print(nums[ N - 1])

except:
    print(-1)
''''
네번째풀이
'''
import sys
from itertools import combinations



nums = list()

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)

        #아..nums가 아니라 comb에 항목을 추가하고 있었구나... 바본가
        nums.append(int("".join(map(str, comb))))

nums.sort()

try:
    print(nums[N - 1])

except:
    print(-1)

'''
최종풀이
'''        
import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()               # 모든 감소하는 수
for i in range(1, 11):      #  1~10개의 조합 만들기 (0~9개니깐)
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        #
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순

try:
    print(nums[n - 1])
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)



