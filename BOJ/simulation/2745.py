'''
진법변환
'''
def solution():
    N, B = map(str, input().split())
    if N.isdigit():
        print(int(N, int(B)))
    else:
        N = N.lower()
        dict = { char: idx+10  for idx, char in enumerate('abcdefghijklmnopqrstuvwxyz')}
        for char in 'abcdefghijklmnopqrstuvwxyz':
            N.replace(char, str(dict[char]))
        print(int(N, int(B)))
solution()