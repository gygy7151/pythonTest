'''
알파벳 찾기
'''
import string
S = list(input())
str_set = string.ascii_lowercase
for target in str_set:
    if target in S:
        print(S.index(target))
    else:
        print(-1)