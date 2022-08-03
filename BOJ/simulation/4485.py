'''
명령프롬프트
'''
def solution():
    N = 'config.sys'


    str = list(input())
    for _ in range(N-1):
        arr = list(input())
        for i in len(str):
            if arr[i] != str[i]:
                str[i] = '?'
    
    print(''.join(str))

solution()