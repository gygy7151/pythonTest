'''
Contact
정규표현식 :https://wikidocs.net/4308#match 사이트 참조
'''
'''
첫번째풀이 - 33%에서 틀림
'''
import sys
import re
input = sys.stdin.readline

def solution():
    T = int(input())
    p = re.compile('(100+1+|01)+')

    for _ in range(T):
        # 아.. 끝에 공백이 포함될 수 있어서 rstrip()으로 없애야했다.
        case = input().rstrip()
        m = p.fullmatch(case)

        if m:print('YES')
        else:print('NO')
solution()
'''
두번째풀이
'''

import re
import sys
input = sys.stdin.readline

p = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    m = p.fullmatch(input().rstrip())
    if m: print('YES')
    else: print('NO')