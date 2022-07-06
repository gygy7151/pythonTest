'''
Hashing
'''
'''
첫번째 풀이 - MOD M: M으로 나눈 나머지를 구하라는 의미였음
'''
D = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
}
def solution():
    M = int(input())
    L = input()
    return sum(D[L[i]]*(31**i) for i in range(M))
print(solution())