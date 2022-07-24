'''
알파벳갯수
'''
'''
첫번째풀이
'''
from collections import Counter
def solution():
    S = input()
    SS = Counter(S)
    SS = SS.most_common()
    alpha = { x: 0 for x in map(str, 'abcdefghijklmnopqrstuvwxyz') }
    for char, val in SS:
        alpha[char] = val
    
    print(*list(alpha.values()))
        
solution()
